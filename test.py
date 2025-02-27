from flaskbb import create_app
from flaskbb.extensions import db
from flaskbb.auth.services.registration import SendActivationPostProcessor
from flaskbb.user.models import User

# Create the app instance
app = create_app()

# Push the application context
with app.app_context():
    user = User.query.filter_by(username="wakanda1").first()
    print(user)
