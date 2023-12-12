from namehasher import set_hashmap, encode_string, decode_string, encode_list, decode_list, validate_values, \
    hashmap_key_value


def test_encode_string():
    set_hashmap("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")
    # check if given the hashmap string, the correct output is given
    assert "**9 (?##*(;* :0;=?!5;" == encode_string("EEN CORRECTE UITKOMST", str(hashmap_key_value))
    # check if case insesitive input is handle correctly
    assert "*en (orrecte :itkomst" != encode_string("Een Correcte Uitkomst", str(hashmap_key_value))


def test_decode_string():
    set_hashmap("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")
    # check if given hasmap string, the correct decode output is given
    assert "ANDERSOM WERKT OOK" == decode_string("%9)*#5?! ]*#=; ??=", str(hashmap_key_value))
    # check if case insesitive input is handle correctly
    assert "Ook Met Kleine Letters" == decode_string("?ok !et =leine 1etters", str(hashmap_key_value))


def test_encode_list():
    set_hashmap("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")
    # check if given a list of values the encoded output is a list of encoded values
    assert [">0*;*#", ">%9"] == encode_list(["PIETER", "PAN"], str(hashmap_key_value))


def test_decode_list():
    set_hashmap("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")
    # check if given a list of values the decoded output is a list of decoded values
    assert ["PIETER", "PAN"] == decode_list([">0*;*#", ">%9"], str(hashmap_key_value))


def test_validate_values():
    set_hashmap("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")
    # check if the given values are equal based on the provided hashmap
    assert True == validate_values(">0*;*#", "PIETER", str(hashmap_key_value))
    # check if the given values are not equal based on case sensitivity and the provided hashmap
    assert False == validate_values(">0*;*#", "Pieter", str(hashmap_key_value))


if __name__ == "__main__":
    test_encode_string()
    test_decode_string()
    test_encode_list()
    test_decode_list()
    test_validate_values()
