import sys
sys.path.append("../sentimental_analysis/audio/")
import unittest
import audio_analyzer

class sentimentAnalyzerTestCases(unittest.TestCase):
    
    # Setup
    def setup(self):
        self.aa = audio_analyzer.AudioAnalyzer()
        self.fa = face_analyzer.FaceAnalyzer()
        self.da = document_analyzer.DocumentAnalyzer()

    # Test case for speech_to_text method
    def test_speech_to_text(self):
        aa = audio_analyzer.AudioAnalyzer()
        self.assertEqual(aa.speech_to_text("test_wv.wav"), "hello how are you")

    # Test case for sentiment_analyzer_scores method
    def test_sentiment_analyzer_scores(self):
        aa = audio_analyzer.AudioAnalyzer()
        self.assertEqual(aa.sentiment_analyzer_scores("hello how are you")["pos"], 0)
        
    def test_textanalysis_post(self, mock_detailed_analysis):
        mock_detailed_analysis.return_value = {'pos': 0.6, 'neu': 0.2, 'neg': 0.2}

        self.client.force_login(self.user)
        data = {'Text': 'This is a test text.'}
        response = self.client.post(reverse('textanalysis'), data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'realworld/sentiment_graph.html')
        mock_detailed_analysis.assert_called_once_with(['This is a test text.'])
        
    def test_productanalysis_post(self, mock_detailed_analysis):
        mock_detailed_analysis.return_value = {'pos': 0.4, 'neu': 0.3, 'neg': 0.3}

        self.client.force_login(self.user)
        data = {'blogname': 'https://example.com/product'}
        response = self.client.post(reverse('productanalysis'), data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'realworld/sentiment_graph.html')
        mock_detailed_analysis.assert_called_once()
    
    def test_reddit_analysis_post(self, mock_detailed_analysis):
        mock_detailed_analysis.return_value = {'pos': 0.5, 'neu': 0.3, 'neg': 0.2}

        self.client.force_login(self.user)
        data = {'keyword': 'python'}
        response = self.client.post(reverse('reddit_analysis'), data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'realworld/sentiment_graph.html')
        mock_detailed_analysis.assert_called_once()

    def test_ytcaptions_post(self, mock_detailed_analysis):
        mock_detailed_analysis.return_value = {'pos': 0.6, 'neu': 0.2, 'neg': 0.2}

        self.client.force_login(self.user)
        data = {'ytid': 'abc123'}
        response = self.client.post(reverse('ytcaptions'), data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'realworld/sentiment_graph.html')
        mock_detailed_analysis.assert_called_once()
        
    def test_ytanalysis_post(self, mock_detailed_analysis):
        mock_detailed_analysis.return_value = {'pos': 0.5, 'neu': 0.3, 'neg': 0.2}

        self.client.force_login(self.user)
        data = {'ytid': 'abc123'}
        response = self.client.post(reverse('ytanalysis'), data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'realworld/sentiment_graph.html')
        mock_detailed_analysis.assert_called_once()
        
    def test_faceAnalysis_post(self, mock_detailed_analysis):
        fa = face_analyzer.FaceAnalyzer()
        self.client.force_login(self.user)
        self.assertEqual(aa.get_face_analysis("photo.jpg"), {'angry': 28.152820467948914, 'disgust': 0.07459266926161945, 'fear': 7.343382388353348, 'happy': 0.00881423256942071, 'sad': 51.542818546295166, 'surprise': 0.30702848453074694, 'neutral': 12.570548057556152})

    def test_documentAnalysis_post(self, mock_detailed_analysis):
        da = document_analyzer.DocumentAnalyzer()
        self.client.force_login(self.user)
        self.assertEqual(da.input("document.pdf"), {'pos': 0.07604527235674442, 'neu': 0.9128369107191668, 'neg': 0.011117816924088688})
    
    def test_index_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_index_not_authenticated(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    #    
    def test_register_post(self):
        data = {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)

# main function
if __name__ == '__main__':
     unittest.main()
