require "./intervalos"

describe Intervalos do

    before(:all) do
        @i = Intervalos.new    
    end        
    
    describe "#get_intervalo" do        
        
        it "retorna o menor intervalo possivel" do            
            @i.get_intervalo([1]).should == [[1]]
        end
        
        it "retorna um intervalo com dois numeros" do
            @i.get_intervalo([1,2]).should == [[1,2]]
        end
        
        it "retorna intervalo mesmo sem estar ordenado" do
            @i.get_intervalo([2,1]).should == [[1,2]]
        end
        
        it "retorna dois valores que nao sejam intervalo" do
            @i.get_intervalo([3,5]).should == [[3],[5]]
        end
        
        it "retorna dois valores que nao sejam intervalo 2" do
            @i.get_intervalo([4,6]).should == [[4],[6]]
        end
        
        it "retorna um intervalo" do
            @i.get_intervalo([3,4,5]).should == [[3,5]]
        end
        
        it "retorna um intervalo 2" do
            @i.get_intervalo([1,2,3,4]).should == [[1,4]]
        end
        
        it "retorna dois intervalos" do
            @i.get_intervalo([1,2,4,5]).should ==[[1,2],[4,5]]
        end
    end
end
