# Generated by Django 3.2.23 on 2024-01-27 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0002_author_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(choices=[('1', 'BOOK1'), ('2', 'BOOK2'), ('3', 'BOOK3'), ('4', 'BOOK4'), ('5', 'BOOK5'), ('6', 'BOOK6'), ('7', 'BOOK7'), ('8', 'BOOK8'), ('9', 'BOOK9'), ('10', 'BOOK10'), ('11', 'BOOK11'), ('12', 'BOOK12'), ('13', 'BOOK13'), ('14', 'BOOK14'), ('15', 'BOOK15'), ('16', 'BOOK16'), ('17', 'BOOK17'), ('18', 'BOOK18'), ('19', 'BOOK19'), ('20', 'BOOK20'), ('21', 'BOOK21'), ('22', 'BOOK22'), ('23', 'BOOK23'), ('24', 'BOOK24'), ('25', 'BOOK25'), ('26', 'BOOK26'), ('27', 'BOOK27'), ('28', 'BOOK28'), ('29', 'BOOK29'), ('30', 'BOOK30'), ('31', 'BOOK31'), ('32', 'BOOK32'), ('33', 'BOOK33'), ('34', 'BOOK34'), ('35', 'BOOK35'), ('36', 'BOOK36'), ('37', 'BOOK37'), ('38', 'BOOK38'), ('39', 'BOOK39'), ('40', 'BOOK40'), ('41', 'BOOK41'), ('42', 'BOOK42'), ('43', 'BOOK43'), ('44', 'BOOK44'), ('45', 'BOOK45'), ('46', 'BOOK46'), ('47', 'BOOK47'), ('48', 'BOOK48'), ('49', 'BOOK49'), ('50', 'BOOK50'), ('51', 'BOOK51'), ('52', 'BOOK52'), ('53', 'BOOK53'), ('54', 'BOOK54'), ('55', 'BOOK55'), ('56', 'BOOK56'), ('57', 'BOOK57'), ('58', 'BOOK58'), ('59', 'BOOK59'), ('60', 'BOOK60'), ('61', 'BOOK61'), ('62', 'BOOK62'), ('63', 'BOOK63'), ('64', 'BOOK64'), ('65', 'BOOK65'), ('66', 'BOOK66'), ('67', 'BOOK67'), ('68', 'BOOK68'), ('69', 'BOOK69'), ('70', 'BOOK70'), ('71', 'BOOK71'), ('72', 'BOOK72'), ('73', 'BOOK73'), ('74', 'BOOK74'), ('75', 'BOOK75'), ('76', 'BOOK76'), ('77', 'BOOK77'), ('78', 'BOOK78'), ('79', 'BOOK79'), ('80', 'BOOK80'), ('81', 'BOOK81'), ('82', 'BOOK82'), ('83', 'BOOK83'), ('84', 'BOOK84'), ('85', 'BOOK85'), ('86', 'BOOK86'), ('87', 'BOOK87'), ('88', 'BOOK88'), ('89', 'BOOK89'), ('90', 'BOOK90'), ('91', 'BOOK91'), ('92', 'BOOK92'), ('93', 'BOOK93'), ('94', 'BOOK94'), ('95', 'BOOK95'), ('96', 'BOOK96'), ('97', 'BOOK97'), ('98', 'BOOK98'), ('99', 'BOOK99')], max_length=10, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('author_email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.author')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]