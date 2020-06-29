from lg import Remote

if __name__ == "__main__":
    address, name = Remote.find_tvs(first_only=True)
    remote = Remote(address)

    key = input('Enter pairing key: ')
    remote.set_pairing_key(key)

    remote.send_command(Remote.VOLUME_UP)
