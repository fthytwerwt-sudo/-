import React from 'react';
import {Composition, Still} from 'remotion';
import {GuidedProofToolchain} from './GuidedProofToolchain';
import {NewFourthReferenceMigrationClip} from './NewFourthReferenceMigrationClip';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Still
        id="GuidedProofToolchainStill"
        component={GuidedProofToolchain}
        width={1920}
        height={1080}
      />
      <Composition
        id="GuidedProofToolchain5s"
        component={GuidedProofToolchain}
        durationInFrames={150}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="NewFourthReferenceMigrationClip"
        component={NewFourthReferenceMigrationClip}
        durationInFrames={1233}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
