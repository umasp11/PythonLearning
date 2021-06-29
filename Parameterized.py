import pytest

# using fixture
@pytest.fixture(params=["a", "b"])
def demo(request):
    print(request.param)


def test_login(demo):
    print('login successfull')


#Using mark
test_data= [(3,5,8), (20,40,60), (40,50,90)]
@pytest.mark.parametrize("ip,op,to", test_data)
def calculator(ip, op, to):
    assert ip+op==to

