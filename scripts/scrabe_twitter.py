#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import gtstore

#Variables that contains the user credentials to access Twitter API
api_key = 'kWAVt64eBo8nmn3tkFsvJaJi3'
api_secret_key = 'MxL5AU6n9QQ2cI8ZgaCeQQcVmmkF0e73am2jPj8TwXB8JUXdT5'
token = '1106257453472272386-C0u9WkSdNekHV8GsiowsT2b7xFkVe4'
secret_token = 'hPvzr47FvhfIehqicMmjkIMFcqPXt2RwjAcY8VG7h4jMZ'

access_token = token
access_token_secret = secret_token
consumer_key = api_key
consumer_secret = api_secret_key


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    connection = gtstore.Twitterdb('gruntwitter.sqlite')
    def on_data(self, data):
        connection.store(data)
        return True

    def on_error(self, status):
        print(status)



if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=['Groningen'])
