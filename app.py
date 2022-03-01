from app import create_app



def main():
    """

    :return:
    """
    app = create_app()
    app.run(host=app.config['LISTENHOST'])


if __name__ == '__main__':
    main()
