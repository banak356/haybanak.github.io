from flask import Flask, render_template, request

app = Flask(__name__)

# Գլխավոր էջ
@app.route('/')
def home():
    return render_template('index.html')

# Նորությունների էջ
@app.route('/news')
def news():
    return render_template('news.html')

# Կապի էջ
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        # Հաղորդագրությունների մշակման լոգիկա
        return f"Շնորհակալություն հաղորդագրության համար, {name}!"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
