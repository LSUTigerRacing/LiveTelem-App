from flask import Blueprint

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/telemetry")
def telemetry():
    # TODO: fields
    #   t                                                optional: s since start, or s/ms epoch
    #   motor_power, motor_torque, motor_rpm             W, Nm, rpm
    #   motor_temp, inverter_temp                        °C
    #   speed, gps_speed                                 km/h
    #   throttle, brake                                  %
    #   steer                                            °
    #   linpot_fl, linpot_fr, linpot_rl, linpot_rr       mm
    #   tire_fl, tire_fr, tire_rl, tire_rr               °C
    #   rotor_fl, rotor_fr, rotor_rl, rotor_rr           °C
    #   rad_in, rad_out                                  °C  (rad_delta is computed by the dashboard)
    #   flow_rate                                        L/min
    #   ax, ay, az                                       g
    #   gx, gy, gz                                       °/s
    #   gps_lat, gps_lon                                 decimal degrees (track map)

    pass
