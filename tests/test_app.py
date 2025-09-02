import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client

def test_health(client):
    res = client.get('/api/health')
    assert res.status_code == 200
    assert res.get_json()['status'] == 'ok'

def test_add_and_list_workouts(client):
    # missing fields
    res = client.post('/api/workouts', json={})
    assert res.status_code == 400

    # bad type for duration
    res = client.post('/api/workouts', json={'workout': 'run', 'duration': 'thirty'})
    assert res.status_code == 400

    # happy path
    res = client.post('/api/workouts', json={'workout': 'run', 'duration': 30})
    assert res.status_code == 201
    body = res.get_json()
    assert body['entry'] == {'workout': 'run', 'duration': 30}

    res = client.get('/api/workouts')
    assert res.status_code == 200
    data = res.get_json()
    assert data['count'] == 1
    assert data['workouts'][0]['workout'] == 'run'
    assert data['workouts'][0]['duration'] == 30