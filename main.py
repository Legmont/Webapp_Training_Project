from app import create_app

#run to start software
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
