from inr_to_usd import inr_to_usd, usd_to_inr  
def test_inr_to_usd():  
       assert inr_to_usd(980) == 10 
def test_usd_to_inr():   
          assert usd_to_inr(10) == 980  
def test_zero_conversion():   
              assert inr_to_usd(0) == 0   
              assert usd_to_inr(0) == 0 