#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
#include "flashgg/DataFormats/interface/MonoHTag.h"
#include "CommonTools/CandUtils/interface/AddFourMomenta.h"

using namespace flashgg;

MonoHTag::MonoHTag() {}

MonoHTag::~MonoHTag() {}

MonoHTag::MonoHTag( edm::Ptr<flashgg::DiPhotonCandidate> diPho, edm::Ptr<DiPhotonMVAResult> mvaRes ) :
    MonoHTag::MonoHTag( diPho, *mvaRes ) {}

MonoHTag::MonoHTag( edm::Ptr<DiPhotonCandidate> dipho, DiPhotonMVAResult mvares ) :
    DiPhotonTagBase::DiPhotonTagBase( dipho, mvares ) {}

void MonoHTag::setMet( edm::Ptr<pat::MET> met )
{
    theMet_ = met;
}

// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

