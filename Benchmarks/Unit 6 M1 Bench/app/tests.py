from django.test import TestCase
from .models import StreamingPlatform, Show, create_streaming_platform, create_show, add_new_season, where_to_watch, what_to_watch, total_shows

# Create your tests here.
class StreamingTest(TestCase):
    def setUp(self) -> None:
        self.streamingservice1 = create_streaming_platform("Hulu", 5)
        self.streamingservice2 = create_streaming_platform("NootFlox", 10)
        self.streamingservice3 = create_streaming_platform("OnlyPans Cooking Network", 30)
        
        self.show1 = create_show("show1", "test1", "horror", self.streamingservice1)
        self.show2 = create_show("show2", "test2", "cooking", self.streamingservice2)
        
        
        
    def test_create_streaming_platform(self):
        platform = create_streaming_platform("amazoom prome", 1)
        self.assertEqual(platform.name, "amazoom prome")
        self.assertEqual(platform.monthly_price, 1)
        
    def test_create_show(self):
        show = create_show("Fast5000", "another fast movie", "racing", self.streamingservice1)
        self.assertEqual(show.name, "Fast5000")
        self.assertEqual(show.service,self.streamingservice1 )
        
    def test_add_new_season(self):
        test = add_new_season("show1")
        self.assertEqual(test, 2)
    
    def test_where_to_watch(self):
        test = where_to_watch("show1")
        self.assertEqual(test, "Hulu")
        
    def test_what_to_watch(self):
        test = what_to_watch(self.streamingservice2, "cooking")
        self.assertEqual(test.count(), 1)
        
    def test_total_shows(self):
        test = total_shows(self.streamingservice3)
        self.assertEqual(test.count(), 0 )
    
