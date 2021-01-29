# Generated by Django 2.1.1 on 2021-01-27 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tally', '0035_auto_20201206_0709'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllCandidatesVotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tally_id', models.IntegerField()),
                ('full_name', models.CharField(max_length=255)),
                ('ballot_number', models.IntegerField()),
                ('candidate_id', models.IntegerField()),
                ('candidate_active', models.BooleanField(default=False)),
                ('stations', models.PositiveIntegerField(default=0)),
                ('center_id', models.IntegerField()),
                ('center_code', models.IntegerField()),
                ('station_number', models.PositiveSmallIntegerField(
                    blank=True, null=True)),
                ('station_id', models.IntegerField()),
                ('stations_completed', models.PositiveIntegerField(default=0)),
                ('votes', models.PositiveIntegerField(default=0)),
                ('total_votes', models.PositiveIntegerField(default=0)),
                ('all_candidate_votes', models.PositiveIntegerField(default=0)),
                ('candidate_votes_included_quarantine', models.PositiveIntegerField(default=0)),
                ('stations_complete_percent', models.IntegerField()),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.RunSQL(
            """
            CREATE MATERIALIZED VIEW tally_allcandidatesvotes AS
            SELECT "tally_candidate"."full_name", "tally_tally"."id" AS "tally_id", "tally_ballot"."number" AS "ballot_number", "tally_candidate"."id" AS "candidate_id", "tally_candidate"."active" AS "candidate_active", COUNT("tally_resultform"."id") FILTER (WHERE ("tally_resultform"."ballot_id" IS NOT NULL AND "tally_resultform"."center_id" IS NOT NULL AND "tally_resultform"."station_number" IS NOT NULL AND "tally_resultform"."tally_id" = ("tally_tally"."id"))) AS "stations", (SELECT U3."code" FROM "tally_resultform" U0 INNER JOIN "tally_ballot" U1 ON (U0."ballot_id" = U1."id") LEFT OUTER JOIN "tally_center" U3 ON (U0."center_id" = U3."id") WHERE (U1."number" = ("tally_ballot"."number") AND U0."tally_id" = ("tally_tally"."id"))  LIMIT 1) AS "center_code", (SELECT U0."center_id" FROM "tally_resultform" U0 INNER JOIN "tally_ballot" U1 ON (U0."ballot_id" = U1."id") WHERE (U1."number" = ("tally_ballot"."number") AND U0."tally_id" = ("tally_tally"."id"))  LIMIT 1) AS "center_id", "tally_resultform"."station_number" AS "station_number", (SELECT U0."id" FROM "tally_station" U0 INNER JOIN "tally_center" U1 ON (U0."center_id" = U1."id") WHERE (U1."code" = ((SELECT U3."code" FROM "tally_resultform" U0 INNER JOIN "tally_ballot" U1 ON (U0."ballot_id" = U1."id") LEFT OUTER JOIN "tally_center" U3 ON (U0."center_id" = U3."id") WHERE (U1."number" = ("tally_ballot"."number") AND U0."tally_id" = ("tally_tally"."id"))  LIMIT 1)) AND U0."tally_id" = ("tally_tally"."id"))  LIMIT 1) AS "station_id", COUNT("tally_resultform"."id") FILTER (WHERE ("tally_resultform"."ballot_id" IS NOT NULL AND "tally_resultform"."center_id" IS NOT NULL AND "tally_resultform"."form_state" = 0 AND "tally_resultform"."station_number" IS NOT NULL AND "tally_resultform"."tally_id" = ("tally_tally"."id"))) AS "stations_completed", (SELECT CASE WHEN U0."votes" IS NOT NULL THEN U0."votes" ELSE 0 END AS "candidate_votes" FROM "tally_result" U0 INNER JOIN "tally_candidate" U1 ON (U0."candidate_id" = U1."id") INNER JOIN "tally_resultform" U3 ON (U0."result_form_id" = U3."id") WHERE (U0."active" = true AND U0."candidate_id" = ("tally_candidate"."id") AND U1."tally_id" = ("tally_tally"."id") AND U0."entry_version" = 2 AND U3."form_state" = 0)  LIMIT 1) AS "votes", CASE WHEN (SELECT CASE WHEN U0."votes" IS NOT NULL THEN U0."votes" ELSE 0 END AS "candidate_votes" FROM "tally_result" U0 INNER JOIN "tally_candidate" U1 ON (U0."candidate_id" = U1."id") INNER JOIN "tally_resultform" U3 ON (U0."result_form_id" = U3."id") WHERE (U0."active" = true AND U0."candidate_id" = ("tally_candidate"."id") AND U1."tally_id" = ("tally_tally"."id") AND U0."entry_version" = 2 AND U3."form_state" = 0)  LIMIT 1) IS NOT NULL THEN (SELECT CASE WHEN U0."votes" IS NOT NULL THEN U0."votes" ELSE 0 END AS "candidate_votes" FROM "tally_result" U0 INNER JOIN "tally_candidate" U1 ON (U0."candidate_id" = U1."id") INNER JOIN "tally_resultform" U3 ON (U0."result_form_id" = U3."id") WHERE (U0."active" = true AND U0."candidate_id" = ("tally_candidate"."id") AND U1."tally_id" = ("tally_tally"."id") AND U0."entry_version" = 2 AND U3."form_state" = 0)  LIMIT 1) ELSE 0 END AS "total_votes", (SELECT CASE WHEN U0."votes" IS NOT NULL THEN U0."votes" ELSE 0 END AS "candidate_votes" FROM "tally_result" U0 INNER JOIN "tally_candidate" U1 ON (U0."candidate_id" = U1."id") INNER JOIN "tally_resultform" U3 ON (U0."result_form_id" = U3."id") WHERE (U0."active" = true AND U0."candidate_id" = ("tally_candidate"."id") AND U1."tally_id" = ("tally_tally"."id") AND U0."entry_version" = 2 AND (U3."form_state" = 0 OR U3."form_state" = 2))  LIMIT 1) AS "all_candidate_votes", CASE WHEN (SELECT CASE WHEN U0."votes" IS NOT NULL THEN U0."votes" ELSE 0 END AS "candidate_votes" FROM "tally_result" U0 INNER JOIN "tally_candidate" U1 ON (U0."candidate_id" = U1."id") INNER JOIN "tally_resultform" U3 ON (U0."result_form_id" = U3."id") WHERE (U0."active" = true AND U0."candidate_id" = ("tally_candidate"."id") AND U1."tally_id" = ("tally_tally"."id") AND U0."entry_version" = 2 AND (U3."form_state" = 0 OR U3."form_state" = 2))  LIMIT 1) IS NOT NULL THEN (SELECT CASE WHEN U0."votes" IS NOT NULL THEN U0."votes" ELSE 0 END AS "candidate_votes" FROM "tally_result" U0 INNER JOIN "tally_candidate" U1 ON (U0."candidate_id" = U1."id") INNER JOIN "tally_resultform" U3 ON (U0."result_form_id" = U3."id") WHERE (U0."active" = true AND U0."candidate_id" = ("tally_candidate"."id") AND U1."tally_id" = ("tally_tally"."id") AND U0."entry_version" = 2 AND (U3."form_state" = 0 OR U3."form_state" = 2))  LIMIT 1) ELSE 0 END AS "candidate_votes_included_quarantine", CASE WHEN COUNT("tally_resultform"."id") FILTER (WHERE ("tally_resultform"."ballot_id" IS NOT NULL AND "tally_resultform"."center_id" IS NOT NULL AND "tally_resultform"."station_number" IS NOT NULL AND "tally_resultform"."tally_id" = ("tally_tally"."id"))) > 0 THEN ROUND(CAST(((100 * CAST(COUNT("tally_resultform"."id") FILTER (WHERE ("tally_resultform"."ballot_id" IS NOT NULL AND "tally_resultform"."center_id" IS NOT NULL AND "tally_resultform"."form_state" = 0 AND "tally_resultform"."station_number" IS NOT NULL AND "tally_resultform"."tally_id" = ("tally_tally"."id"))) AS FLOAT)) / CAST(COUNT("tally_resultform"."id") FILTER (WHERE ("tally_resultform"."ballot_id" IS NOT NULL AND "tally_resultform"."center_id" IS NOT NULL AND "tally_resultform"."station_number" IS NOT NULL AND "tally_resultform"."tally_id" = ("tally_tally"."id"))) AS FLOAT)) AS numeric), 3) ELSE 0 END AS "stations_complete_percent" FROM "tally_tally" LEFT OUTER JOIN "tally_ballot" ON ("tally_tally"."id" = "tally_ballot"."tally_id") LEFT OUTER JOIN "tally_candidate" ON ("tally_ballot"."id" = "tally_candidate"."ballot_id") LEFT OUTER JOIN "tally_resultform" ON ("tally_ballot"."id" = "tally_resultform"."ballot_id") WHERE "tally_tally"."active" = true GROUP BY "tally_tally"."id", "tally_ballot"."number", "tally_candidate"."id", (SELECT U3."code" FROM "tally_resultform" U0 INNER JOIN "tally_ballot" U1 ON (U0."ballot_id" = U1."id") LEFT OUTER JOIN "tally_center" U3 ON (U0."center_id" = U3."id") WHERE (U1."number" = ("tally_ballot"."number") AND U0."tally_id" = ("tally_tally"."id"))  LIMIT 1), (SELECT U0."center_id" FROM "tally_resultform" U0 INNER JOIN "tally_ballot" U1 ON (U0."ballot_id" = U1."id") WHERE (U1."number" = ("tally_ballot"."number") AND U0."tally_id" = ("tally_tally"."id"))  LIMIT 1), "tally_resultform"."station_number", (SELECT U0."id" FROM "tally_station" U0 INNER JOIN "tally_center" U1 ON (U0."center_id" = U1."id") WHERE (U1."code" = ((SELECT U3."code" FROM "tally_resultform" U0 INNER JOIN "tally_ballot" U1 ON (U0."ballot_id" = U1."id") LEFT OUTER JOIN "tally_center" U3 ON (U0."center_id" = U3."id") WHERE (U1."number" = ("tally_ballot"."number") AND U0."tally_id" = ("tally_tally"."id"))  LIMIT 1)) AND U0."tally_id" = ("tally_tally"."id"))  LIMIT 1), (SELECT CASE WHEN U0."votes" IS NOT NULL THEN U0."votes" ELSE 0 END AS "candidate_votes" FROM "tally_result" U0 INNER JOIN "tally_candidate" U1 ON (U0."candidate_id" = U1."id") INNER JOIN "tally_resultform" U3 ON (U0."result_form_id" = U3."id") WHERE (U0."active" = true AND U0."candidate_id" = ("tally_candidate"."id") AND U1."tally_id" = ("tally_tally"."id") AND U0."entry_version" = 2 AND U3."form_state" = 0)  LIMIT 1), CASE WHEN (SELECT CASE WHEN U0."votes" IS NOT NULL THEN U0."votes" ELSE 0 END AS "candidate_votes" FROM "tally_result" U0 INNER JOIN "tally_candidate" U1 ON (U0."candidate_id" = U1."id") INNER JOIN "tally_resultform" U3 ON (U0."result_form_id" = U3."id") WHERE (U0."active" = true AND U0."candidate_id" = ("tally_candidate"."id") AND U1."tally_id" = ("tally_tally"."id") AND U0."entry_version" = 2 AND U3."form_state" = 0)  LIMIT 1) IS NOT NULL THEN (SELECT CASE WHEN U0."votes" IS NOT NULL THEN U0."votes" ELSE 0 END AS "candidate_votes" FROM "tally_result" U0 INNER JOIN "tally_candidate" U1 ON (U0."candidate_id" = U1."id") INNER JOIN "tally_resultform" U3 ON (U0."result_form_id" = U3."id") WHERE (U0."active" = true AND U0."candidate_id" = ("tally_candidate"."id") AND U1."tally_id" = ("tally_tally"."id") AND U0."entry_version" = 2 AND U3."form_state" = 0)  LIMIT 1) ELSE 0 END, (SELECT CASE WHEN U0."votes" IS NOT NULL THEN U0."votes" ELSE 0 END AS "candidate_votes" FROM "tally_result" U0 INNER JOIN "tally_candidate" U1 ON (U0."candidate_id" = U1."id") INNER JOIN "tally_resultform" U3 ON (U0."result_form_id" = U3."id") WHERE (U0."active" = true AND U0."candidate_id" = ("tally_candidate"."id") AND U1."tally_id" = ("tally_tally"."id") AND U0."entry_version" = 2 AND (U3."form_state" = 0 OR U3."form_state" = 2))  LIMIT 1), CASE WHEN (SELECT CASE WHEN U0."votes" IS NOT NULL THEN U0."votes" ELSE 0 END AS "candidate_votes" FROM "tally_result" U0 INNER JOIN "tally_candidate" U1 ON (U0."candidate_id" = U1."id") INNER JOIN "tally_resultform" U3 ON (U0."result_form_id" = U3."id") WHERE (U0."active" = true AND U0."candidate_id" = ("tally_candidate"."id") AND U1."tally_id" = ("tally_tally"."id") AND U0."entry_version" = 2 AND (U3."form_state" = 0 OR U3."form_state" = 2))  LIMIT 1) IS NOT NULL THEN (SELECT CASE WHEN U0."votes" IS NOT NULL THEN U0."votes" ELSE 0 END AS "candidate_votes" FROM "tally_result" U0 INNER JOIN "tally_candidate" U1 ON (U0."candidate_id" = U1."id") INNER JOIN "tally_resultform" U3 ON (U0."result_form_id" = U3."id") WHERE (U0."active" = true AND U0."candidate_id" = ("tally_candidate"."id") AND U1."tally_id" = ("tally_tally"."id") AND U0."entry_version" = 2 AND (U3."form_state" = 0 OR U3."form_state" = 2))  LIMIT 1) ELSE 0 END;
            CREATE UNIQUE INDEX tally_allcandidatesvotes_pk ON tally_allcandidatesvotes(tally_id);
            """,
            """
            DROP MATERIALIZED VIEW tally_allcandidatesvotes;
            """
        ),
    ]
