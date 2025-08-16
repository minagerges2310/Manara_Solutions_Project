from flask import Flask, render_template
import requests

# This line initializes the Flask application.
app = Flask(__name__)

def get_instance_id():
    """Fetches the EC2 instance ID from the metadata service using IMDSv2."""
    instance_id = "N/A"
    try:
        # This line sends a PUT request to get a session token for secure metadata access.
        token_response = requests.put(
            'http://169.254.169.254/latest/api/token',
            headers={'X-aws-ec2-metadata-token-ttl-seconds': '21600'},
            timeout=2
        )
        token = token_response.text
        
        # This line prepares the header with the session token for the next request.
        headers = {'X-aws-ec2-metadata-token': token}
        # This line sends a GET request with the token to retrieve the instance ID.
        instance_id_response = requests.get(
            'http://169.254.169.254/latest/meta-data/instance-id',
            headers=headers,
            timeout=2
        )
        instance_id = instance_id_response.text
    except requests.exceptions.RequestException:
        instance_id = "Error: Could not fetch Instance ID"
    return instance_id

@app.route('/')
def home():
    """This function handles requests to the main page."""
    instance_id = get_instance_id()
    # This line renders the HTML template, passing the instance ID to it.
    return render_template('index.html', instance_id=instance_id)

if __name__ == '__main__':
    # This line starts the web server on port 80, accessible from any IP address.
    app.run(host='0.0.0.0', port=80)
