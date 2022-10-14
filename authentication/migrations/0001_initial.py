# Generated by Django 4.1 on 2022-10-13 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("username", models.CharField(max_length=255)),
                (
                    "phonenumber",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("fullname", models.CharField(blank=True, max_length=200, null=True)),
                ("address", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "profilepicture",
                    models.ImageField(
                        blank=True, null=True, upload_to="profilepicture/"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=255, null=True, unique=True
                    ),
                ),
                ("is_verified", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "user_role",
                    models.CharField(
                        choices=[
                            ("user", "user"),
                            ("vendor", "vendor"),
                            ("superuser", "superuser"),
                        ],
                        default="user",
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("auth_provider", models.CharField(default="email", max_length=255)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
