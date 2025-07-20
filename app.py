from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

# In-memory storage for entries (replace with DB for production)
entries = []
avatars = ['user1.png', 'user2.png', 'default.png']  # example avatars

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        message = request.form.get('message', '').strip()
        avatar = request.form.get('avatar', 'default.png')
        if not name or not message:
            # Simple validation
            return render_template('index.html', entries=entries, error="Name and message required.", avatars=avatars)

        # Create new entry with ID = len(entries)
        entry = {
            'id': len(entries),
            'name': name,
            'message': message,
            'avatar': avatar if avatar in avatars else 'default.png'
        }
        entries.append(entry)
        return redirect(url_for('index'))

    return render_template('index.html', entries=entries, avatars=avatars, error=None)

@app.route('/entry/<int:entry_id>')
def entry_detail(entry_id):
    if entry_id < 0 or entry_id >= len(entries):
        abort(404)
    entry = entries[entry_id]
    return render_template('entry.html', entry=entry)

if __name__ == "__main__":
    app.run(debug=True)
