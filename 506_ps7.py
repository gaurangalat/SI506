# import statements
import unittest
import json
import requests
import pickle
import webbrowser
from pprint import pprint

print "\n***** PART 1: Classes Mechanics *****\n"

# [PROBLEM 1]
print "\n***** PROBLEM 1 *****\n"

# Here is a class definition to represent a photo object. Take a look at the code and make sure you understand it.

class Photo():
    def __init__(self, title, author, tags):
        self.title = title
        self.author = author
        self.tags = tags

# HINT: if you just call the constructor for the Photo class appropriately, everything will be taken care of for you. You just have to figure out, from the definition of the class, what to pass to the constructor. Remember the examples of creating a class instance from the textbook!

# Write your one line of code here:
my_photo=Photo("Photo1","Ansel Adams",['Nature','Mist','Mountain'])

# [PROBLEM 2]
print "\n***** PROBLEM 2 *****\n"

# We have provided a sample dictionary in the format that Flickr returns it. Let's read it in from a file. Feel free to add some print statements to understand the structure of sample_diction. You may also find it useful to open the file "sample_diction.txt" in a text editor, or copy and paste its contents into http://www.jsoneditoronline.org/

## Do not change these next 3 lines of code!
f = open("sample_diction.txt", "r")
sample_diction = json.loads(f.read())
f.close()

# Your job is to fill in the __init__ method
class Photo2():
    def __init__(self, photo_d):
         # fill in this method!
         self.title=photo_d["photo"]["title"]["_content"]
         self.author=photo_d["photo"]["owner"]["username"]
         self.tags=[]
         for i in photo_d["photo"]["tags"]["tag"]:
            self.tags.append(i["raw"])
# After you fill it in, try creating an instance by invoking Photo2(sample_diction) and check to see if it has the values you expect for title, author, and tags.
my_photo2=Photo2(sample_diction)

### PART 2: FlickR Tag Recommender
print "\n***** PART 2: FlickR Tag Recommender *****\n"


flickr_key = "42db68c806beca06a382236c54bc791a" # paste your flickr key here, so the variable flickr_key contains a string (your flickr key!)
if not flickr_key:
    flickr_key = raw_input("Enter your flickr API key, or paste it in the .py file to avoid this prompt in the future: \n>>")

## Useful function definitions provided for you below.

cache_fname = "cached_results.txt"
try:
    fobj = open(cache_fname, 'rb')
    saved_cache = pickle.load(fobj)
    fobj.close()
except:
    raise Exception("Make sure you have cached_results.txt in the same directory as this code file. You should be using it for this problem set!")
    #saved_cache = {}

def canonical_order(d):
    alphabetized_keys = sorted(d.keys())
    res = []
    for k in alphabetized_keys:
        res.append((k, d[k]))
    return res

def requestURL(baseurl, params = {}):
    req = requests.Request(method = 'GET', url = baseurl, params = canonical_order(params))
    prepped = req.prepare()
    return prepped.url

def get_with_caching(base_url, params_diction, cache_diction, cache_fname, omitted_keys = ['api_key']):
    filtered_params_diction = {}
    for k in params_diction:
        if k not in omitted_keys:
            filtered_params_diction[k] = params_diction[k]
    full_url = requestURL(base_url, filtered_params_diction)
    if full_url in cache_diction:
        print "retrieving data from the API associated with " + full_url
        return cache_diction[full_url]
    else:
        response = requests.get(base_url, params=params_diction)
        print "adding saved data to cache file for " + full_url
        # add to the cache and save it permanently
        cache_diction[full_url] = response.text
        fobj = open(cache_fname, "wb")
        pickle.dump(cache_diction, fobj)
        fobj.close()
        return response.text


## [PROBLEM 3]
print "\n***** PROBLEM 3 *****\n"
## See the textbook section on the flickr API, and see the documentation page at https://www.flickr.com/services/api/flickr.photos.search.html

base_url = "https://api.flickr.com/services/rest/"

cache_fname="cache_results_1.txt"

params_d = {}
params_d['method'] = 'flickr.photos.search'
params_d['api_key'] = flickr_key
params_d['format'] = 'json'
params_d['tags'] = ['sunset']
params_d['tag_mode'] = 'all'
params_d['per_page'] = 50

try:
    fobj = open(cache_fname, 'r')
    saved_cache = pickle.load(fobj)
    fobj.close()
except:
    saved_cache = {}
resp_text = get_with_caching('https://api.flickr.com/services/rest/', params_diction=params_d, cache_diction = saved_cache, cache_fname = cache_fname)
search_result_diction = json.loads(resp_text[14:-1])


# #[PROBLEM 4] 
print "\n***** PROBLEM 4 *****\n"
# You should rely on search_result_diction as your variable, NOT flickr_info. The textbook instructions will shortly be updated to reflect this.

# photo_ids_list
photo_ids_list=[]
for i in search_result_diction["photos"]["photo"]:
    photo_ids_list.append(i['id'])

params_d['method'] = 'flickr.photos.getInfo'
photo_instances=[]
for i in photo_ids_list:
    params_d['photo_id']=i
    try:
        esp_text = get_with_caching('https://api.flickr.com/services/rest/', params_diction=params_d, cache_diction = saved_cache, cache_fname = cache_fname)
        diction2 = json.loads(esp_text[14:-1])
        test2=Photo2(diction2)
        photo_instances.append(test2)
    except:
        continue


# [PROBLEM 5] 
print "\n***** PROBLEM 5 *****\n"

counts_diction={}
for photos in photo_instances:
    for i in photos.tags:
        if i not in counts_diction:
            counts_diction[i]=0
        counts_diction[i]+=1

# [PROBLEM 6]
print "\n***** PROBLEM 6 *****\n"

listoftuple=[]
sorted_tags=[]
for (a,b) in counts_diction.items():
    listoftuple.append((a,b))

sorted_tags1=sorted(listoftuple, key=lambda x: (-x[1],x[0]))

for i in sorted_tags1:
    sorted_tags.append(i[0])

# [PROBLEM 7] Output five recommended tags
print "\n***** PROBLEM 7 *****\n"

## Print, for the user to see, the five tags (other than the searched on tag, sunset) that were used MOST frequently!

# [PROBLEM 7] Output five recommended tags
most_common_tags=sorted_tags[1:6]
print "Below this line, the 5 most frequently used tags should print out:"
print most_common_tags
print "-----------------done; output of diagnostic tests is below this line------------"
##### Code for running diagnostic tests are below this line. Don't change any code below this line######
class Problem1(unittest.TestCase):
    def test_title(self):
        self.assertEqual(my_photo.title, "Photo1")
    def test_author(self):
        self.assertEqual(my_photo.author, "Ansel Adams")
    def test_tags(self):
        self.assertEqual(my_photo.tags, ['Nature', 'Mist', 'Mountain'])

class Problem2(unittest.TestCase):
    def setUp(self):
        f = open("sample_diction.txt", "r")
        sample_diction = json.loads(f.read())
        f.close()
        self.p2 = Photo2(sample_diction)

    def test_title(self):
        self.assertEqual(self.p2.title, "Photo1")
    def test_author(self):
        self.assertEqual(self.p2.author, "Ansel Adams")
    def test_tags(self):
        self.assertEqual(self.p2.tags, ['Nature', 'Mist', 'Mountain'])

class Problem3(unittest.TestCase):
    def test_prefix(self):
        print "\nNote that if you are getting an invalid JSON object error, check that you're dealing with the 'jsonFlickrApi(' text that begins data you get from the Flickr API. Check out the flickr_demo example on Canvas!\n"
    def test_01(self):
        self.assertIn('photos',search_result_diction, "Check if 'photos' is a key" )
    def test_02(self):
        self.assertIn('photo',search_result_diction['photos'], "Check for search_result_diction['photos']['photo']")
    def test_03_check_length(self):
        self.assertEqual(len(search_result_diction['photos']['photo']), 50, "check if 50 photos returned")

class Problem4(unittest.TestCase):

    def test_01(self):
        self.assertEqual(len(photo_ids_list), 50, "Check id count")

    def test_02(self):
        self.assertEqual(photo_ids_list[0], "30602056932", "Check first id")

    def test_03(self):
        self.assertEqual(len(photo_instances), 50, "Check count")

    def test_04(self):
        self.assertEqual(photo_instances[0].tags[:3], [u'Brook Bay', u'Dusk', u'England'], "Check tags of first instance")

class Problem5(unittest.TestCase):

    def test_01(self):
        self.assertEqual(counts_diction['sul'], 1, "testing count for the key 'sul'")
        self.assertEqual(counts_diction['Sky'], 2, "testing that the count for the key sunset is 50")

class Problems6and7(unittest.TestCase):

    def test_01(self):
        self.assertEqual(sorted_tags[:10], [u'sunset', u'Sunset', u'Architecture', u'Italy', u'Travel', u'Boats', u'Europe', u'Garda', u'Lake', u'Lazise'], "Check your sorted tags")
    def test_02(self):
        self.assertEqual(sorted_tags[0],u'sunset',"Checking whether the first element in your sorted tags list is 'sunset'")


unittest.main(verbosity=2)

