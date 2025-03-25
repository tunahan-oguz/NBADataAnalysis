from django.test import TestCase
from django.urls import reverse
from ..models import PlayerBio, CareerAwards, LeagueLeaders, PlayerHeadShot
from ..forms import PlayerSearchForm, TeamSearchForm, PlayerCompareForm
from ..functions import player_regular_season, player_post_season

class PlayerBioTests(TestCase):
    def setUp(self):
        self.player = PlayerBio.objects.create(
            player_id=1,
            player_name="LeBron James",
            position="F",
            weight=250.0,
            year=2003,
            number=23,
            team_id=1610612737,  # Lakers ID
            PTS=27.1,
            REB=7.5,
            AST=7.3,
            BLK=0.8,
            STL=1.5
        )

    def test_player_name(self):
        self.assertEqual(self.player.player_name, "LeBron James")

    def test_player_position(self):
        self.assertEqual(self.player.position, "F")

    def test_player_stats(self):
        self.assertEqual(self.player.PTS, 27.1)
        self.assertEqual(self.player.REB, 7.5)
        self.assertEqual(self.player.AST, 7.3)

class CareerAwardsTests(TestCase):
    def setUp(self):
        self.award = CareerAwards.objects.create(
            player_id=2,
            player_name="Test Player",
            accomplishments={
                "MVP": ["2023-24"],
                "All-Star": ["2022-23", "2023-24"]
            }
        )

    def test_award_creation(self):
        self.assertEqual(self.award.player_name, "Test Player")
        self.assertIn("MVP", self.award.accomplishments)
        self.assertEqual(len(self.award.accomplishments["All-Star"]), 2)

class LeagueLeadersTests(TestCase):
    def setUp(self):
        self.leaders = LeagueLeaders.objects.create(
            leaders={
                "points": [
                    {"player_name": "Test Player", "value": 30.0, "rank": 1}
                ]
            }
        )

    def test_leader_creation(self):
        self.assertIn("points", self.leaders.leaders)
        self.assertEqual(self.leaders.leaders["points"][0]["player_name"], "Test Player")
        self.assertEqual(self.leaders.leaders["points"][0]["value"], 30.0)

class ViewsTests(TestCase):
    def setUp(self):
        self.player = PlayerBio.objects.create(
            player_id=3,
            player_name="Test View Player",
            position="G",
            weight=210.0,
            year=2010,
            number=10,
            team_id=1610612737,
            PTS=15.0,
            REB=4.0,
            AST=5.5,
            BLK=0.3,
            STL=1.2
        )
class PlayerSearchFormTest(TestCase):
    
    # Geçerli bir oyuncu ismi girildiğinde form geçerli olmalı
    def test_valid_input(self):
        form = PlayerSearchForm({'player_name': 'LeBron James'})
        self.assertTrue(form.is_valid())  # ✔️ Form geçerli mi?

    # Oyuncu ismi boş bırakıldığında form geçersiz olmalı
    def test_invalid_empty(self):
        form = PlayerSearchForm({'player_name': ''})
        self.assertFalse(form.is_valid())  # ❌ Form geçerli değil çünkü required


# TeamSearchForm'u test ediyoruz
class TeamSearchFormTest(TestCase):

    # Geçerli bir takım ismi girildiğinde form geçerli olmalı
    def test_valid_input(self):
        form = TeamSearchForm({'team_name': 'Lakers'})
        self.assertTrue(form.is_valid())  # ✔️

    # Takım ismi boş bırakıldığında form geçersiz olmalı
    def test_invalid_empty(self):
        form = TeamSearchForm({'team_name': ''})
        self.assertFalse(form.is_valid())  # ❌


# PlayerCompareForm'u test ediyoruz (iki oyuncu karşılaştırılıyor)
class PlayerCompareFormTest(TestCase):

    # Her iki oyuncu adı da girildiyse form geçerli olmalı
    def test_valid_players(self):
        form = PlayerCompareForm({'player1': 'Curry', 'player2': 'Durant'})
        self.assertTrue(form.is_valid())  # ✔️

class PlayerStatsFunctionTest(TestCase):

    # Bu test, player_regular_season fonksiyonunun doğru bir liste döndürüp döndürmediğini kontrol eder
    def test_regular_season_returns_data(self):
        player_id = 201939  # Stephen Curry'nin oyuncu ID'si

        # Fonksiyonu çağır ve dönen istatistikleri al
        stats = player_regular_season(player_id)

        # stats nesnesi bir liste olmalı
        self.assertIsInstance(stats, list)

        # Liste boş olmamalı, en az bir sezon verisi olmalı
        self.assertGreater(len(stats), 0)

    # Bu test, player_post_season fonksiyonunun bir liste döndürüp döndürmediğini kontrol eder
    def test_post_season_returns_data(self):
        player_id = 201939  # Yine Curry'nin ID'si

        # Playoff istatistiklerini al
        stats = player_post_season(player_id)

        # stats yine bir liste olmalı
        self.assertIsInstance(stats, list)

        # NOT: Burada length kontrolü yok çünkü bazı oyuncuların hiç playoff verisi olmayabilir
class PlayerHeadShotModelTest(TestCase):

    # Bu test, team_id'ye göre background_colour otomatik olarak doğru atanıyor mu kontrol eder
    def test_background_colour_on_save(self):
        # Örnek bir PlayerHeadShot objesi oluşturuluyor
        # team_id = 1610612737 → Bu "Hawks" takımının ID'si
        shot = PlayerHeadShot(
            player_id=123,
            player_name="Test Player",
            team_id=1610612737  # Bu ID modeldeki TEAM_COLOURS sözlüğünde tanımlı
        )

        # Modeldeki save() metodu çağrıldığında, background_colour otomatik ayarlanmalı
        shot.save()

        # Beklenen renk, TEAM_COLOURS sözlüğünde Hawks için tanımlı olan '#e03a3e'
        self.assertEqual(shot.background_colour, '#e03a3e')
