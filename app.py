from flask import Flask, render_template, request, url_for, redirect
import ThermoApp
from threading import Thread
import _thread

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'
##Move relay control to start on server start
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == "GET":
        ThermoApp.read_temp()
        tt = ThermoApp.get_cur_temp()
        ti = ThermoApp.get_time()
        trgt = ThermoApp.SetTargetTemp()
        mode = ThermoApp.SetThermoMode()
            
        tnt = {'cur_temp':tt,'cur_time':ti, 'targ_temp':trgt, 'mode':mode}
        return render_template('dashboard.html', tnt=tnt)
    elif request.method == "POST":
        
        try:
            temp = request.form['target_temp']
            ThermoApp.SetTargetTemp(temp)
        except:
            print("cannot set target temp")
        try:
            mode = request.form['thermo_mode']
            ThermoApp.SetThermoMode(mode)
        except:
            print("cannot set Thermo Mode")
            
        _thread.start_new_thread(ThermoApp.RelayControl, ())
        return redirect(url_for('dashboard'))
            
        
        

        
        
        
if __name__ == '__main__':
    _thread.start_new_thread(ThermoApp.RunThermoApp, ())
    app.run(debug=True, host='10.0.0.34', threaded=True)
    
