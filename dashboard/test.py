from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import WeatherStation

class DashboardTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        self.station = WeatherStation.objects.create(
            name='Test Station',
            location='Test Location',
            api_key='test-api-key-123',
            user=self.user
        )
    
    def test_dashboard_view(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')
    
    def test_add_station_view(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('add_station'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/add_station.html')
    
    def test_station_creation(self):
        self.client.login(username='testuser', password='testpassword123')
        data = {
            'name': 'New Test Station',
            'location': 'New Test Location',
            'api_key': 'new-test-api-key-123'
        }
        response = self.client.post(reverse('add_station'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(WeatherStation.objects.filter(name='New Test Station').exists())