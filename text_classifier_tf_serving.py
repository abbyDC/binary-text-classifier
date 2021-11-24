import requests
import json

# usual format for sending post requests through tf srving
# if ever a different model is served, no need to change anything here
def post_request(url, instances):
    data = json.dumps({"instances": instances})
    json_response = requests.post(url, data=data)
    predictions = json.loads(json_response.text).get('predictions')
	
    return predictions

# url to send the post request
url = 'http://localhost:8501/v1/models/tf_nnlm:predict'
# sentences to be evaluated
instances = ["Ito ay nasa tagalog"]
predictions = post_request(url, instances)
for x in predictions:
	if round(x[0],0) == 1:
		print(f"Text: {instances[0]} \nClass: English")
	else:
		print(f"Text: {instances[0]} \nClass: Tagalog")


