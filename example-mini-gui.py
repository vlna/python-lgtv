from lg import Remote
import tkinter as tk
import configparser

def volume_up():
    remote.send_command(Remote.VOLUME_UP)

def volume_down():
    remote.send_command(Remote.VOLUME_DOWN)

def channel_up():
    remote.send_command(Remote.CHANNEL_UP)

def channel_down():
    remote.send_command(Remote.CHANNEL_DOWN)

if __name__ == "__main__":
    address, name = Remote.find_tvs(first_only=True)
    remote = Remote(address)

    config = configparser.ConfigParser()
    config.read('.python-lgtv.ini')

    if 'default' not in config.sections():
        pairing_key = input('Insert pairing key: ')
        remote.set_pairing_key(pairing_key)
        if remote.get_session():
            config.add_section('default')
            config.set('default', 'pairing_key', pairing_key)
            config.set('default', 'name', name)
            with open('.python-lgtv.ini', 'w') as configfile:
                config.write(configfile)
    else:
        if config['default']['name']==name:
            remote.set_pairing_key(config['default']['pairing_key'])

    window = tk.Tk()
    window.title(name)

    mini = tk.Frame(master=window, width=50, height=50)

    mini_buttons =[tk.Button(master=window, text=x[0], command=x[1],
                   width=10, height=3, bg="white", fg="black",
                   font=("Courier", 22)) for x in [('VOL+', volume_up),
                                                   ('CH+', channel_up),
                                                   ('VOL-', volume_down),
                                                   ('CH-', channel_down)]]

    for i,o in enumerate(mini_buttons):
        o.grid(row=i//2, column=i%2, padx=10, pady=10)

    window.mainloop()
