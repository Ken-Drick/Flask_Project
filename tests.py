import unittest
import warnings
from api import app


class MyAppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_index_page(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "<p>Welcome, Kendrick!</p>")
    
#TEST READ
    def test_get_movies(self):
        response = self.app.get("/movies")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Toy Story (1995)" in response.data.decode())
     
    def test_get_movies_by_id(self):
        response = self.app.get("/movies/3")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Grumpier Old Men (1995)" in response.data.decode())
        
    def test_get_movies_by_id(self):
        response = self.app.get("/movies/9/UserHist")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Sudden Death (1995)" in response.data.decode())
#TEST CREATE     
    def test_add_movie(self):
        data = {
            "title": "Spider-Man 2 (2004)",
            "genres": "Action|Sci-fi"
        }
        response = self.app.post("/movies", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue("the movie was added successfully" in response.data.decode())
        
#TEST UPDATE        
    def test_update_movie(self):
        movieId = 5  # ID of the movie to update
        data = {
            "title": "Father of the Bride Part 2 (1995)",
            "genres": "Comedy|Family"
        }
        response = self.app.put(f"/movies/{movieId}", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("The movie was updated successfully" in response.data.decode())
    

#TEST DELETE
    def test_delete_movie(self):
        movieId = 650
        response = self.app.delete(f"/movies/{movieId}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("The movie was deleted successfully" in response.data.decode())
     
        
            
if __name__ == "__main__":
    unittest.main()