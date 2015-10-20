#ifndef FLASHgg_MonoHTag_h
#define FLASHgg_MonoHTag_h

#include "DataFormats/PatCandidates/interface/MET.h"
#include "flashgg/DataFormats/interface/DiPhotonTagBase.h"

namespace flashgg {

    class MonoHTag: public DiPhotonTagBase
    {
    public:
        MonoHTag();
        ~MonoHTag();

        MonoHTag *clone() const { return ( new MonoHTag( *this ) ); }

        MonoHTag( edm::Ptr<DiPhotonCandidate>, edm::Ptr<DiPhotonMVAResult> );
        MonoHTag( edm::Ptr<DiPhotonCandidate>, DiPhotonMVAResult );

        const edm::Ptr<pat::MET> met() const {return theMet_;}
        const edm::Ptr<DiPhotonCandidate> diPhotonCandidate() const { return theDiPhotonCandidate_;}
        void setMet( edm::Ptr<pat::MET> );

    private:
        edm::Ptr<DiPhotonCandidate> theDiPhotonCandidate_;
        edm::Ptr<pat::MET> theMet_;
    };

}

#endif
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

