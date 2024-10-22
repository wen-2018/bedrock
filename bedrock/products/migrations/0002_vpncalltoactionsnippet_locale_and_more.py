# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Generated by Django 4.2.16 on 2024-10-09 09:53

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailcore", "0093_uploadedfile"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="vpncalltoactionsnippet",
            name="locale",
            field=models.ForeignKey(
                default=1, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name="+", to="wagtailcore.locale"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="vpncalltoactionsnippet",
            name="translation_key",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterUniqueTogether(
            name="vpncalltoactionsnippet",
            unique_together={("translation_key", "locale")},
        ),
    ]