require "./palavras"

describe Palavras do
    
    before(:all) do
        @palavra = Palavras.new
    end
        
    describe "#is_primo" do
    
      it "teste com menor numero primo" do
         @palavra.is_primo("b").should be_true
      end        
       
    end
end

describe Fixnum do
    
    describe "is_prime?" do
        it "deve ser primo" do
            1.is_prime?.should be_true
        end
    end   
    
end
