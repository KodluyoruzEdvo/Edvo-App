from flask import Flask, request, jsonify, send_file

from jinja2 import Template
app = Flask(__name__)


secenekler = [0,0,0,0]
araliklar = [(100,350),(450,700),(1200,1450),(1550,1800)]

users = {}


def canvas(x=500, y=500, degisken=5):
    t = Template('''
    <script
    src="https://code.jquery.com/jquery-3.5.1.js"
    integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc="
    crossorigin="anonymous"></script>
    <style>    .Rrrrr { font: italic 60px serif; fill: white; }</style>
    <svg style='stroke-width: 0px; background-image: url(http://localhost:5001/geti); background-size: 1900px; background-color: rgb(176,241,235);' height="900" width="1900">

     <rect x="0" width="1900" rx="15" height="100" style="fill:rgb(6, 53, 15);stroke-width:3;stroke:rgb(236,236,236)"></rect>
     <foreignobject x="0" y="0" width="1900" height="100" font-size="46px" color="white">
         <body xmlns="http://www.w3.org/1999/xhtml">
                <div style="text-align: center; ">En sevdiginiz hayvan</div>
                <div style="position:absolute; left: 20px; top: 20px;" id="test"></div>
     </foreignobject>


<rect x="100" y="175" width="250" rx="15" height="650" style="fill:rgb(32, 154, 166);stroke-width:3;stroke:rgb(249,249,249)"></rect>
<foreignObject x="100" y="175" width="250" height="700" font-size="46px" color="white">
         <div style="text-align: center; ">Aslan</div>
         <div style="text-align: center; "><br><br><br><br><br><br><br><br><br>
    <span id="0">0</span></div>
</foreignObject>


<rect x="450" y="175" width="250" rx="15" height="650" style="fill:rgb(243, 105, 89);stroke-width:3;stroke:rgb(245,245,245)"></rect>
<foreignObject x="450" y="175" width="250" height="700" font-size="46px" color="white">
<div style="text-align: center; ">Kaplan</div>
         <div style="text-align: center; "><br><br><br><br><br><br><br><br><br>
         <span id="1">0</span>
    </div>

</foreignObject>

<rect x="700" y="100" "width="100" rx="15" height="100" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)"></rect>
<rect x="1200" y="175" width="250" rx="15" height="650" style="fill:rgb(140,140,218);stroke-width:3;stroke:rgb(255,255,255)"></rect>
<foreignObject x="1200" y="175" width="250" height="700" font-size="46px" color="white">
         <div style="text-align: center; ">Kedi</div>
<div style="text-align: center; "><br><br><br><br><br><br><br><br><br>
    <span id="2">0</span></div>
</foreignObject>
<rect x="1550" y="175" width="250" rx="15" height="650" style="fill:rgb(243,173,128);stroke-width:3;stroke:rgb(255,255,255)"></rect>
<foreignObject id="4" x="1550" y="175" width="250" height="700" font-size="46px" color="white">
         <div style="text-align: center; ">Puma</div>
         <div style="text-align: center; "><br><br><br><br><br><br><br><br><br> <span id="3">0</span></div>
</foreignObject>

</svg>

    <script>

        var name = window.prompt("username", "");
        $('text').html(name);

        if (name !== ''){
            var res = '';
            $(document).keydown(function(e){
                if (e.which == 37) {
                    console.log("left pressed");
                    res = 'left'
                }
                else if (e.which == 38) {
                    console.log("up pressed");
                    res = 'up'
            }
                else if (e.which == 39) {
                    console.log("right pressed");
                    res = 'right'
            }
                else if (e.which == 40) {
                    console.log("down pressed");
                    res = 'down'
            }
                $.post({
                    url: '/',
                    data: {'username': name, 'direction': res},
                    success: function(data) {
                        var secenekler = data['secenekler']
                        data = data['users']

                        Object.keys(data).forEach(function(username) {
                            var _data = data[username];
                            if ( !$('#' + username + '_circle').length) {
                                $('svg').append('<circle id="' + username + '_circle" cx="100" cy="100" r="40" stroke="#F6EF00" stroke-width="3" fill="#F6EF00" />');
                                $('svg').append('<text id="' + username + '_text" x="100" y="100" font-family="sans-serif" font-size="20px" fill="black">' + username + '</text>');
                            }
                            console.log(_data);

                            $('#' + username + '_circle').attr(_data);
                            $('#' + username + '_text').attr({x: _data.cx-20, y: parseInt(_data.cy)+8});
                            $("svg").html($("svg").html());

                        })
                    }
                });
            });
        }


        var y = setInterval(function(){
            $.post({
                url: '/son_durum',
                data: {},
                success: function(data) {
                    var secenekler = data['secenekler']
                    for (var i=0; i < secenekler.length; i++){
                        $('#' + i).text(secenekler[i]);
                    }
                    data = data['users']
                    console.log(secenekler)
                    Object.keys(data).forEach(function(username) {
                        var _data = data[username];
                        if ( !$('#' + username + '_circle').length) {
                            $('svg').append('<circle id="' + username + '_circle" cx="100" cy="100" r="40" stroke="#F6EF00" stroke-width="3" fill="#F6EF00" />');
                            $('svg').append('<text id="' + username + '_text" x="100" y="100" font-family="sans-serif" font-size="20px" fill="black">' + username + '</text>');
                        }
                        console.log(_data);

                        $('#' + username + '_circle').attr(_data);
                        $('#' + username + '_text').attr({x: _data.cx-20, y: parseInt(_data.cy)+8});
                        $("svg").html($("svg").html());

                    })
                }
            });
        }, 1000)

var x = setInterval(function () {
    var d = new Date();
    var seconds = d.getMinutes() * 60 + d.getSeconds(); //convet 00:00 to seconds for easier caculation
    var fiveMin = 60 * 1; //five minutes is 300 seconds!
    var timeleft = fiveMin - seconds % fiveMin; // let's say 01:30, then current seconds is 90, 90%300 = 90, then 300-90 = 210. That's the time left!
    var result = parseInt(timeleft / 60) + ':' + timeleft % 60; //formart seconds into 00:00
    document.getElementById('test').innerHTML = result;

    if (timeleft === 1) {
        clearInterval(x);
        clearInterval(y);
        document.getElementById("test").innerHTML = "ZAMAN DOLDU";

      }
}, 500)
</script>

    ''')
    return t.render(degisken=degisken)
import time
@app.route('/index', methods=['POST', 'GET'])
def index():
    i = 0
    return canvas(500, 500,i)

@app.route('/geti')
def geti():
    filename = 'edvo.png'
    return send_file(filename, mimetype='image/jpg')

@app.route('/', methods=['POST', 'GET'])
def home():

    username = request.form.get('username')

    if username not in users:
        users[username] = {'cx': 950, 'cy': 390}

    x = users[username].get('cx')
    y = users[username].get('cy')

    if request.form.get('direction') == 'up':
        y = y - 5
    if request.form.get('direction') == 'down':
        y = y + 5
    if request.form.get('direction') == 'left':
        x = x - 5
    if request.form.get('direction') == 'right':
        x = x + 5
    users[username] = {'cx': x, 'cy': y}

    return {'users':users,'secenekler':secenekler}

def y_araliginda(y):
    return (200 < y < 800)

def xn_araliginda(x):
    index = 0
    for aralik in araliklar:
        if (aralik[0] < x < aralik[1]):
            return index
        index = index + 1



@app.route('/son_durum', methods=['POST', 'GET'])
def araba():
    #{u'oguz': {'cy': 390, 'cx': 950}}
    for user,koordinat in users.items():
        if y_araliginda(koordinat['cy']):
            aralik = xn_araliginda(koordinat['cx'])
            if aralik==0 or aralik:
                secenekler[aralik] = secenekler[aralik] + 1

    return {'users':users,'secenekler':secenekler}


app.run(host='0.0.0.0',port='5001')

