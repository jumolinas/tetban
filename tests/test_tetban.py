
from pytest import raises
from tetban.main import TetBanTest

def test_tetban():
    # test tetban without any subcommands or arguments
    with TetBanTest() as app:
        app.run()
        assert app.exit_code == 0


def test_tetban_debug():
    # test that debug mode is functional
    argv = ['--debug']
    with TetBanTest(argv=argv) as app:
        app.run()
        assert app.debug is True


def test_command1():
    # test command1 without arguments
    argv = ['command1']
    with TetBanTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['foo'] == 'bar'
        assert output.find('Foo => bar')


    # test command1 with arguments
    argv = ['command1', '--foo', 'not-bar']
    with TetBanTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['foo'] == 'not-bar'
        assert output.find('Foo => not-bar')
