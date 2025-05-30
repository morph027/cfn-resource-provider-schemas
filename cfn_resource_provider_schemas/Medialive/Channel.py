SCHEMA = {
  "typeName" : "AWS::MediaLive::Channel",
  "description" : "Resource Type definition for AWS::MediaLive::Channel",
  "additionalProperties" : False,
  "properties" : {
    "InputAttachments" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/InputAttachment"
      }
    },
    "InputSpecification" : {
      "$ref" : "#/definitions/InputSpecification"
    },
    "Destinations" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/OutputDestination"
      }
    },
    "DryRun" : {
      "type" : "boolean"
    },
    "Vpc" : {
      "$ref" : "#/definitions/VpcOutputSettings"
    },
    "ChannelEngineVersion" : {
      "$ref" : "#/definitions/ChannelEngineVersionRequest"
    },
    "Maintenance" : {
      "$ref" : "#/definitions/MaintenanceCreateSettings"
    },
    "LogLevel" : {
      "type" : "string"
    },
    "RoleArn" : {
      "type" : "string"
    },
    "Name" : {
      "type" : "string"
    },
    "ChannelClass" : {
      "type" : "string"
    },
    "EncoderSettings" : {
      "$ref" : "#/definitions/EncoderSettings"
    },
    "AnywhereSettings" : {
      "$ref" : "#/definitions/AnywhereSettings"
    },
    "CdiInputSpecification" : {
      "$ref" : "#/definitions/CdiInputSpecification"
    },
    "Id" : {
      "type" : "string"
    },
    "Arn" : {
      "type" : "string"
    },
    "Inputs" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "type" : "string"
      }
    },
    "Tags" : {
      "type" : "object"
    }
  },
  "definitions" : {
    "AudioSelectorSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AudioLanguageSelection" : {
          "$ref" : "#/definitions/AudioLanguageSelection"
        },
        "AudioTrackSelection" : {
          "$ref" : "#/definitions/AudioTrackSelection"
        },
        "AudioPidSelection" : {
          "$ref" : "#/definitions/AudioPidSelection"
        },
        "AudioHlsRenditionSelection" : {
          "$ref" : "#/definitions/AudioHlsRenditionSelection"
        }
      }
    },
    "InputLocation" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "PasswordParam" : {
          "type" : "string"
        },
        "Username" : {
          "type" : "string"
        },
        "Uri" : {
          "type" : "string"
        }
      }
    },
    "FrameCaptureGroupSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FrameCaptureCdnSettings" : {
          "$ref" : "#/definitions/FrameCaptureCdnSettings"
        },
        "Destination" : {
          "$ref" : "#/definitions/OutputLocationRef"
        }
      }
    },
    "Ac3Settings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CodingMode" : {
          "type" : "string"
        },
        "DrcProfile" : {
          "type" : "string"
        },
        "MetadataControl" : {
          "type" : "string"
        },
        "Dialnorm" : {
          "type" : "integer"
        },
        "LfeFilter" : {
          "type" : "string"
        },
        "BitstreamMode" : {
          "type" : "string"
        },
        "AttenuationControl" : {
          "type" : "string"
        },
        "Bitrate" : {
          "type" : "number"
        }
      }
    },
    "AudioDolbyEDecode" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ProgramSelection" : {
          "type" : "string"
        }
      }
    },
    "AudioCodecSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Eac3Settings" : {
          "$ref" : "#/definitions/Eac3Settings"
        },
        "Ac3Settings" : {
          "$ref" : "#/definitions/Ac3Settings"
        },
        "Mp2Settings" : {
          "$ref" : "#/definitions/Mp2Settings"
        },
        "Eac3AtmosSettings" : {
          "$ref" : "#/definitions/Eac3AtmosSettings"
        },
        "PassThroughSettings" : {
          "$ref" : "#/definitions/PassThroughSettings"
        },
        "WavSettings" : {
          "$ref" : "#/definitions/WavSettings"
        },
        "AacSettings" : {
          "$ref" : "#/definitions/AacSettings"
        }
      }
    },
    "UdpGroupSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TimedMetadataId3Frame" : {
          "type" : "string"
        },
        "TimedMetadataId3Period" : {
          "type" : "integer"
        },
        "InputLossAction" : {
          "type" : "string"
        }
      }
    },
    "MediaPackageOutputDestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ChannelName" : {
          "type" : "string"
        },
        "ChannelId" : {
          "type" : "string"
        },
        "ChannelGroup" : {
          "type" : "string"
        }
      }
    },
    "Scte20PlusEmbeddedDestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "H264Settings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TimecodeBurninSettings" : {
          "$ref" : "#/definitions/TimecodeBurninSettings"
        },
        "NumRefFrames" : {
          "type" : "integer"
        },
        "TemporalAq" : {
          "type" : "string"
        },
        "Slices" : {
          "type" : "integer"
        },
        "FramerateControl" : {
          "type" : "string"
        },
        "QvbrQualityLevel" : {
          "type" : "integer"
        },
        "FramerateNumerator" : {
          "type" : "integer"
        },
        "ParControl" : {
          "type" : "string"
        },
        "GopClosedCadence" : {
          "type" : "integer"
        },
        "FlickerAq" : {
          "type" : "string"
        },
        "Profile" : {
          "type" : "string"
        },
        "QualityLevel" : {
          "type" : "string"
        },
        "MinIInterval" : {
          "type" : "integer"
        },
        "SceneChangeDetect" : {
          "type" : "string"
        },
        "ForceFieldPictures" : {
          "type" : "string"
        },
        "FramerateDenominator" : {
          "type" : "integer"
        },
        "Softness" : {
          "type" : "integer"
        },
        "GopSize" : {
          "type" : "number"
        },
        "AdaptiveQuantization" : {
          "type" : "string"
        },
        "FilterSettings" : {
          "$ref" : "#/definitions/H264FilterSettings"
        },
        "MinQp" : {
          "type" : "integer"
        },
        "ColorSpaceSettings" : {
          "$ref" : "#/definitions/H264ColorSpaceSettings"
        },
        "EntropyEncoding" : {
          "type" : "string"
        },
        "SpatialAq" : {
          "type" : "string"
        },
        "ParDenominator" : {
          "type" : "integer"
        },
        "FixedAfd" : {
          "type" : "string"
        },
        "GopSizeUnits" : {
          "type" : "string"
        },
        "AfdSignaling" : {
          "type" : "string"
        },
        "Bitrate" : {
          "type" : "integer"
        },
        "ParNumerator" : {
          "type" : "integer"
        },
        "RateControlMode" : {
          "type" : "string"
        },
        "ScanType" : {
          "type" : "string"
        },
        "BufSize" : {
          "type" : "integer"
        },
        "TimecodeInsertion" : {
          "type" : "string"
        },
        "ColorMetadata" : {
          "type" : "string"
        },
        "BufFillPct" : {
          "type" : "integer"
        },
        "GopBReference" : {
          "type" : "string"
        },
        "LookAheadRateControl" : {
          "type" : "string"
        },
        "Level" : {
          "type" : "string"
        },
        "MaxBitrate" : {
          "type" : "integer"
        },
        "Syntax" : {
          "type" : "string"
        },
        "SubgopLength" : {
          "type" : "string"
        },
        "GopNumBFrames" : {
          "type" : "integer"
        }
      }
    },
    "FrameCaptureHlsSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "RawSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "KeyProviderSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "StaticKeySettings" : {
          "$ref" : "#/definitions/StaticKeySettings"
        }
      }
    },
    "UdpContainerSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "M2tsSettings" : {
          "$ref" : "#/definitions/M2tsSettings"
        }
      }
    },
    "BandwidthReductionFilterSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "PostFilterSharpening" : {
          "type" : "string"
        },
        "Strength" : {
          "type" : "string"
        }
      }
    },
    "FeatureActivations" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "OutputStaticImageOverlayScheduleActions" : {
          "type" : "string"
        },
        "InputPrepareScheduleActions" : {
          "type" : "string"
        }
      }
    },
    "MultiplexGroupSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "SrtGroupSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "InputLossAction" : {
          "type" : "string"
        }
      }
    },
    "ArchiveGroupSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Destination" : {
          "$ref" : "#/definitions/OutputLocationRef"
        },
        "ArchiveCdnSettings" : {
          "$ref" : "#/definitions/ArchiveCdnSettings"
        },
        "RolloverInterval" : {
          "type" : "integer"
        }
      }
    },
    "ArchiveS3Settings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CannedAcl" : {
          "type" : "string"
        }
      }
    },
    "MultiplexContainerSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MultiplexM2tsSettings" : {
          "$ref" : "#/definitions/MultiplexM2tsSettings"
        }
      }
    },
    "NielsenConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DistributorId" : {
          "type" : "string"
        },
        "NielsenPcmToId3Tagging" : {
          "type" : "string"
        }
      }
    },
    "TeletextSourceSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "OutputRectangle" : {
          "$ref" : "#/definitions/CaptionRectangle"
        },
        "PageNumber" : {
          "type" : "string"
        }
      }
    },
    "CmafIngestGroupSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Destination" : {
          "$ref" : "#/definitions/OutputLocationRef"
        },
        "KlvNameModifier" : {
          "type" : "string"
        },
        "Scte35Type" : {
          "type" : "string"
        },
        "NielsenId3Behavior" : {
          "type" : "string"
        },
        "Scte35NameModifier" : {
          "type" : "string"
        },
        "SegmentLengthUnits" : {
          "type" : "string"
        },
        "NielsenId3NameModifier" : {
          "type" : "string"
        },
        "KlvBehavior" : {
          "type" : "string"
        },
        "SegmentLength" : {
          "type" : "integer"
        },
        "Id3Behavior" : {
          "type" : "string"
        },
        "SendDelayMs" : {
          "type" : "integer"
        },
        "Id3NameModifier" : {
          "type" : "string"
        }
      }
    },
    "AribDestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "CaptionSelectorSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DvbSubSourceSettings" : {
          "$ref" : "#/definitions/DvbSubSourceSettings"
        },
        "Scte27SourceSettings" : {
          "$ref" : "#/definitions/Scte27SourceSettings"
        },
        "AribSourceSettings" : {
          "$ref" : "#/definitions/AribSourceSettings"
        },
        "EmbeddedSourceSettings" : {
          "$ref" : "#/definitions/EmbeddedSourceSettings"
        },
        "Scte20SourceSettings" : {
          "$ref" : "#/definitions/Scte20SourceSettings"
        },
        "TeletextSourceSettings" : {
          "$ref" : "#/definitions/TeletextSourceSettings"
        },
        "AncillarySourceSettings" : {
          "$ref" : "#/definitions/AncillarySourceSettings"
        }
      }
    },
    "GlobalConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "InputEndAction" : {
          "type" : "string"
        },
        "OutputLockingSettings" : {
          "$ref" : "#/definitions/OutputLockingSettings"
        },
        "OutputTimingSource" : {
          "type" : "string"
        },
        "OutputLockingMode" : {
          "type" : "string"
        },
        "SupportLowFramerateInputs" : {
          "type" : "string"
        },
        "InitialAudioGain" : {
          "type" : "integer"
        },
        "InputLossBehavior" : {
          "$ref" : "#/definitions/InputLossBehavior"
        }
      }
    },
    "PipelineLockingSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "FrameCaptureS3Settings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CannedAcl" : {
          "type" : "string"
        }
      }
    },
    "MultiplexM2tsSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Scte35Control" : {
          "type" : "string"
        },
        "PcrPeriod" : {
          "type" : "integer"
        },
        "NielsenId3Behavior" : {
          "type" : "string"
        },
        "EsRateInPes" : {
          "type" : "string"
        },
        "CcDescriptor" : {
          "type" : "string"
        },
        "AudioFramesPerPes" : {
          "type" : "integer"
        },
        "AbsentInputAudioBehavior" : {
          "type" : "string"
        },
        "AudioStreamType" : {
          "type" : "string"
        },
        "Klv" : {
          "type" : "string"
        },
        "Arib" : {
          "type" : "string"
        },
        "AudioBufferModel" : {
          "type" : "string"
        },
        "Ebif" : {
          "type" : "string"
        },
        "Scte35PrerollPullupMilliseconds" : {
          "type" : "number"
        },
        "PcrControl" : {
          "type" : "string"
        }
      }
    },
    "FailoverCondition" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FailoverConditionSettings" : {
          "$ref" : "#/definitions/FailoverConditionSettings"
        }
      }
    },
    "AudioTrackSelection" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DolbyEDecode" : {
          "$ref" : "#/definitions/AudioDolbyEDecode"
        },
        "Tracks" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/AudioTrack"
          }
        }
      }
    },
    "OutputGroup" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Outputs" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/Output"
          }
        },
        "OutputGroupSettings" : {
          "$ref" : "#/definitions/OutputGroupSettings"
        },
        "Name" : {
          "type" : "string"
        }
      }
    },
    "VideoSelectorColorSpaceSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Hdr10Settings" : {
          "$ref" : "#/definitions/Hdr10Settings"
        }
      }
    },
    "AribSourceSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "Mpeg2FilterSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TemporalFilterSettings" : {
          "$ref" : "#/definitions/TemporalFilterSettings"
        }
      }
    },
    "DvbSubSourceSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "OcrLanguage" : {
          "type" : "string"
        },
        "Pid" : {
          "type" : "integer"
        }
      }
    },
    "AudioDescription" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AudioDashRoles" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "LanguageCodeControl" : {
          "type" : "string"
        },
        "CodecSettings" : {
          "$ref" : "#/definitions/AudioCodecSettings"
        },
        "Name" : {
          "type" : "string"
        },
        "AudioWatermarkingSettings" : {
          "$ref" : "#/definitions/AudioWatermarkSettings"
        },
        "AudioNormalizationSettings" : {
          "$ref" : "#/definitions/AudioNormalizationSettings"
        },
        "LanguageCode" : {
          "type" : "string"
        },
        "RemixSettings" : {
          "$ref" : "#/definitions/RemixSettings"
        },
        "AudioSelectorName" : {
          "type" : "string"
        },
        "StreamName" : {
          "type" : "string"
        },
        "DvbDashAccessibility" : {
          "type" : "string"
        },
        "AudioType" : {
          "type" : "string"
        },
        "AudioTypeControl" : {
          "type" : "string"
        }
      }
    },
    "DvbNitSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "NetworkName" : {
          "type" : "string"
        },
        "NetworkId" : {
          "type" : "integer"
        },
        "RepInterval" : {
          "type" : "integer"
        }
      }
    },
    "VideoSelectorSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "VideoSelectorProgramId" : {
          "$ref" : "#/definitions/VideoSelectorProgramId"
        },
        "VideoSelectorPid" : {
          "$ref" : "#/definitions/VideoSelectorPid"
        }
      }
    },
    "OutputDestination" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SrtSettings" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/SrtOutputDestinationSettings"
          }
        },
        "Id" : {
          "type" : "string"
        },
        "MultiplexSettings" : {
          "$ref" : "#/definitions/MultiplexProgramChannelDestinationSettings"
        },
        "Settings" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/OutputDestinationSettings"
          }
        },
        "MediaPackageSettings" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/MediaPackageOutputDestinationSettings"
          }
        }
      }
    },
    "AudioLanguageSelection" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "LanguageCode" : {
          "type" : "string"
        },
        "LanguageSelectionPolicy" : {
          "type" : "string"
        }
      }
    },
    "AvailSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Scte35SpliceInsert" : {
          "$ref" : "#/definitions/Scte35SpliceInsert"
        },
        "Scte35TimeSignalApos" : {
          "$ref" : "#/definitions/Scte35TimeSignalApos"
        },
        "Esam" : {
          "$ref" : "#/definitions/Esam"
        }
      }
    },
    "AvailBlanking" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "State" : {
          "type" : "string"
        },
        "AvailBlankingImage" : {
          "$ref" : "#/definitions/InputLocation"
        }
      }
    },
    "InputLossBehavior" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "InputLossImageType" : {
          "type" : "string"
        },
        "InputLossImageSlate" : {
          "$ref" : "#/definitions/InputLocation"
        },
        "InputLossImageColor" : {
          "type" : "string"
        },
        "RepeatFrameMsec" : {
          "type" : "integer"
        },
        "BlackFrameMsec" : {
          "type" : "integer"
        }
      }
    },
    "MulticastInputSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SourceIpAddress" : {
          "type" : "string"
        }
      }
    },
    "SrtOutputSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "EncryptionType" : {
          "type" : "string"
        },
        "Destination" : {
          "$ref" : "#/definitions/OutputLocationRef"
        },
        "BufferMsec" : {
          "type" : "integer"
        },
        "ContainerSettings" : {
          "$ref" : "#/definitions/UdpContainerSettings"
        },
        "Latency" : {
          "type" : "integer"
        }
      }
    },
    "HlsMediaStoreSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FilecacheDuration" : {
          "type" : "integer"
        },
        "MediaStoreStorageClass" : {
          "type" : "string"
        },
        "RestartDelay" : {
          "type" : "integer"
        },
        "NumRetries" : {
          "type" : "integer"
        },
        "ConnectionRetryInterval" : {
          "type" : "integer"
        }
      }
    },
    "BlackoutSlate" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "NetworkId" : {
          "type" : "string"
        },
        "NetworkEndBlackoutImage" : {
          "$ref" : "#/definitions/InputLocation"
        },
        "NetworkEndBlackout" : {
          "type" : "string"
        },
        "State" : {
          "type" : "string"
        },
        "BlackoutSlateImage" : {
          "$ref" : "#/definitions/InputLocation"
        }
      }
    },
    "SmpteTtDestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "VideoSelectorProgramId" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ProgramId" : {
          "type" : "integer"
        }
      }
    },
    "CaptionLanguageMapping" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "LanguageCode" : {
          "type" : "string"
        },
        "LanguageDescription" : {
          "type" : "string"
        },
        "CaptionChannel" : {
          "type" : "integer"
        }
      }
    },
    "HlsOutputSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "HlsSettings" : {
          "$ref" : "#/definitions/HlsSettings"
        },
        "NameModifier" : {
          "type" : "string"
        },
        "H265PackagingType" : {
          "type" : "string"
        },
        "SegmentModifier" : {
          "type" : "string"
        }
      }
    },
    "Scte27SourceSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "OcrLanguage" : {
          "type" : "string"
        },
        "Pid" : {
          "type" : "integer"
        }
      }
    },
    "M3u8Settings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "PatInterval" : {
          "type" : "integer"
        },
        "ProgramNum" : {
          "type" : "integer"
        },
        "PcrPeriod" : {
          "type" : "integer"
        },
        "PmtInterval" : {
          "type" : "integer"
        },
        "KlvDataPids" : {
          "type" : "string"
        },
        "NielsenId3Behavior" : {
          "type" : "string"
        },
        "PcrPid" : {
          "type" : "string"
        },
        "VideoPid" : {
          "type" : "string"
        },
        "AudioFramesPerPes" : {
          "type" : "integer"
        },
        "TransportStreamId" : {
          "type" : "integer"
        },
        "PmtPid" : {
          "type" : "string"
        },
        "Scte35Pid" : {
          "type" : "string"
        },
        "Scte35Behavior" : {
          "type" : "string"
        },
        "KlvBehavior" : {
          "type" : "string"
        },
        "EcmPid" : {
          "type" : "string"
        },
        "TimedMetadataPid" : {
          "type" : "string"
        },
        "AudioPids" : {
          "type" : "string"
        },
        "PcrControl" : {
          "type" : "string"
        },
        "TimedMetadataBehavior" : {
          "type" : "string"
        }
      }
    },
    "RtmpGroupSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AuthenticationScheme" : {
          "type" : "string"
        },
        "CacheLength" : {
          "type" : "integer"
        },
        "AdMarkers" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "IncludeFillerNalUnits" : {
          "type" : "string"
        },
        "InputLossAction" : {
          "type" : "string"
        },
        "RestartDelay" : {
          "type" : "integer"
        },
        "CaptionData" : {
          "type" : "string"
        },
        "CacheFullBehavior" : {
          "type" : "string"
        }
      }
    },
    "H264FilterSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TemporalFilterSettings" : {
          "$ref" : "#/definitions/TemporalFilterSettings"
        },
        "BandwidthReductionFilterSettings" : {
          "$ref" : "#/definitions/BandwidthReductionFilterSettings"
        }
      }
    },
    "StandardHlsSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AudioRenditionSets" : {
          "type" : "string"
        },
        "M3u8Settings" : {
          "$ref" : "#/definitions/M3u8Settings"
        }
      }
    },
    "Output" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "OutputSettings" : {
          "$ref" : "#/definitions/OutputSettings"
        },
        "CaptionDescriptionNames" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "AudioDescriptionNames" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "OutputName" : {
          "type" : "string"
        },
        "VideoDescriptionName" : {
          "type" : "string"
        }
      }
    },
    "ChannelEngineVersionRequest" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Version" : {
          "type" : "string"
        }
      }
    },
    "VideoDescription" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ScalingBehavior" : {
          "type" : "string"
        },
        "RespondToAfd" : {
          "type" : "string"
        },
        "Height" : {
          "type" : "integer"
        },
        "Sharpness" : {
          "type" : "integer"
        },
        "Width" : {
          "type" : "integer"
        },
        "CodecSettings" : {
          "$ref" : "#/definitions/VideoCodecSettings"
        },
        "Name" : {
          "type" : "string"
        }
      }
    },
    "FrameCaptureSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TimecodeBurninSettings" : {
          "$ref" : "#/definitions/TimecodeBurninSettings"
        },
        "CaptureIntervalUnits" : {
          "type" : "string"
        },
        "CaptureInterval" : {
          "type" : "integer"
        }
      }
    },
    "AnywhereSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ChannelPlacementGroupId" : {
          "type" : "string"
        },
        "ClusterId" : {
          "type" : "string"
        }
      }
    },
    "ColorCorrectionSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "GlobalColorCorrections" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/ColorCorrection"
          }
        }
      }
    },
    "CdiInputSpecification" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Resolution" : {
          "type" : "string"
        }
      }
    },
    "Esam" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AdAvailOffset" : {
          "type" : "integer"
        },
        "ZoneIdentity" : {
          "type" : "string"
        },
        "AcquisitionPointId" : {
          "type" : "string"
        },
        "PoisEndpoint" : {
          "type" : "string"
        },
        "Username" : {
          "type" : "string"
        },
        "PasswordParam" : {
          "type" : "string"
        }
      }
    },
    "MaintenanceCreateSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MaintenanceDay" : {
          "type" : "string"
        },
        "MaintenanceStartTime" : {
          "type" : "string"
        }
      }
    },
    "InputSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Scte35Pid" : {
          "type" : "integer"
        },
        "DeblockFilter" : {
          "type" : "string"
        },
        "FilterStrength" : {
          "type" : "integer"
        },
        "InputFilter" : {
          "type" : "string"
        },
        "SourceEndBehavior" : {
          "type" : "string"
        },
        "VideoSelector" : {
          "$ref" : "#/definitions/VideoSelector"
        },
        "Smpte2038DataPreference" : {
          "type" : "string"
        },
        "AudioSelectors" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/AudioSelector"
          }
        },
        "CaptionSelectors" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/CaptionSelector"
          }
        },
        "DenoiseFilter" : {
          "type" : "string"
        },
        "NetworkInputSettings" : {
          "$ref" : "#/definitions/NetworkInputSettings"
        }
      }
    },
    "DvbTdtSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "RepInterval" : {
          "type" : "integer"
        }
      }
    },
    "FrameCaptureCdnSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FrameCaptureS3Settings" : {
          "$ref" : "#/definitions/FrameCaptureS3Settings"
        }
      }
    },
    "FecOutputSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ColumnDepth" : {
          "type" : "integer"
        },
        "IncludeFec" : {
          "type" : "string"
        },
        "RowLength" : {
          "type" : "integer"
        }
      }
    },
    "Rec601Settings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "AudioPidSelection" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Pid" : {
          "type" : "integer"
        }
      }
    },
    "H265ColorSpaceSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Rec601Settings" : {
          "$ref" : "#/definitions/Rec601Settings"
        },
        "Rec709Settings" : {
          "$ref" : "#/definitions/Rec709Settings"
        },
        "ColorSpacePassthroughSettings" : {
          "$ref" : "#/definitions/ColorSpacePassthroughSettings"
        },
        "DolbyVision81Settings" : {
          "$ref" : "#/definitions/DolbyVision81Settings"
        },
        "Hdr10Settings" : {
          "$ref" : "#/definitions/Hdr10Settings"
        }
      }
    },
    "VideoCodecSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FrameCaptureSettings" : {
          "$ref" : "#/definitions/FrameCaptureSettings"
        },
        "H264Settings" : {
          "$ref" : "#/definitions/H264Settings"
        },
        "Mpeg2Settings" : {
          "$ref" : "#/definitions/Mpeg2Settings"
        },
        "H265Settings" : {
          "$ref" : "#/definitions/H265Settings"
        },
        "Av1Settings" : {
          "$ref" : "#/definitions/Av1Settings"
        }
      }
    },
    "MediaPackageGroupSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Destination" : {
          "$ref" : "#/definitions/OutputLocationRef"
        }
      }
    },
    "H265FilterSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TemporalFilterSettings" : {
          "$ref" : "#/definitions/TemporalFilterSettings"
        },
        "BandwidthReductionFilterSettings" : {
          "$ref" : "#/definitions/BandwidthReductionFilterSettings"
        }
      }
    },
    "NielsenCBET" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CbetStepaside" : {
          "type" : "string"
        },
        "CbetCheckDigitString" : {
          "type" : "string"
        },
        "Csid" : {
          "type" : "string"
        }
      }
    },
    "OutputGroupSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "HlsGroupSettings" : {
          "$ref" : "#/definitions/HlsGroupSettings"
        },
        "FrameCaptureGroupSettings" : {
          "$ref" : "#/definitions/FrameCaptureGroupSettings"
        },
        "MultiplexGroupSettings" : {
          "$ref" : "#/definitions/MultiplexGroupSettings"
        },
        "SrtGroupSettings" : {
          "$ref" : "#/definitions/SrtGroupSettings"
        },
        "ArchiveGroupSettings" : {
          "$ref" : "#/definitions/ArchiveGroupSettings"
        },
        "MediaPackageGroupSettings" : {
          "$ref" : "#/definitions/MediaPackageGroupSettings"
        },
        "UdpGroupSettings" : {
          "$ref" : "#/definitions/UdpGroupSettings"
        },
        "MsSmoothGroupSettings" : {
          "$ref" : "#/definitions/MsSmoothGroupSettings"
        },
        "RtmpGroupSettings" : {
          "$ref" : "#/definitions/RtmpGroupSettings"
        },
        "CmafIngestGroupSettings" : {
          "$ref" : "#/definitions/CmafIngestGroupSettings"
        }
      }
    },
    "AudioChannelMapping" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "InputChannelLevels" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/InputChannelLevel"
          }
        },
        "OutputChannel" : {
          "type" : "integer"
        }
      }
    },
    "CmafIngestOutputSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "NameModifier" : {
          "type" : "string"
        }
      }
    },
    "NetworkInputSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MulticastInputSettings" : {
          "$ref" : "#/definitions/MulticastInputSettings"
        },
        "ServerValidation" : {
          "type" : "string"
        },
        "HlsInputSettings" : {
          "$ref" : "#/definitions/HlsInputSettings"
        }
      }
    },
    "TeletextDestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "ColorCorrection" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "OutputColorSpace" : {
          "type" : "string"
        },
        "InputColorSpace" : {
          "type" : "string"
        },
        "Uri" : {
          "type" : "string"
        }
      }
    },
    "WebvttDestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "StyleControl" : {
          "type" : "string"
        }
      }
    },
    "UdpOutputSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Destination" : {
          "$ref" : "#/definitions/OutputLocationRef"
        },
        "FecOutputSettings" : {
          "$ref" : "#/definitions/FecOutputSettings"
        },
        "BufferMsec" : {
          "type" : "integer"
        },
        "ContainerSettings" : {
          "$ref" : "#/definitions/UdpContainerSettings"
        }
      }
    },
    "EncoderSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AudioDescriptions" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/AudioDescription"
          }
        },
        "VideoDescriptions" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/VideoDescription"
          }
        },
        "GlobalConfiguration" : {
          "$ref" : "#/definitions/GlobalConfiguration"
        },
        "MotionGraphicsConfiguration" : {
          "$ref" : "#/definitions/MotionGraphicsConfiguration"
        },
        "ThumbnailConfiguration" : {
          "$ref" : "#/definitions/ThumbnailConfiguration"
        },
        "FeatureActivations" : {
          "$ref" : "#/definitions/FeatureActivations"
        },
        "CaptionDescriptions" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/CaptionDescription"
          }
        },
        "AvailConfiguration" : {
          "$ref" : "#/definitions/AvailConfiguration"
        },
        "ColorCorrectionSettings" : {
          "$ref" : "#/definitions/ColorCorrectionSettings"
        },
        "OutputGroups" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/OutputGroup"
          }
        },
        "AvailBlanking" : {
          "$ref" : "#/definitions/AvailBlanking"
        },
        "NielsenConfiguration" : {
          "$ref" : "#/definitions/NielsenConfiguration"
        },
        "BlackoutSlate" : {
          "$ref" : "#/definitions/BlackoutSlate"
        },
        "TimecodeConfig" : {
          "$ref" : "#/definitions/TimecodeConfig"
        }
      }
    },
    "Fmp4HlsSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AudioRenditionSets" : {
          "type" : "string"
        },
        "NielsenId3Behavior" : {
          "type" : "string"
        },
        "TimedMetadataBehavior" : {
          "type" : "string"
        }
      }
    },
    "HlsSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Fmp4HlsSettings" : {
          "$ref" : "#/definitions/Fmp4HlsSettings"
        },
        "FrameCaptureHlsSettings" : {
          "$ref" : "#/definitions/FrameCaptureHlsSettings"
        },
        "StandardHlsSettings" : {
          "$ref" : "#/definitions/StandardHlsSettings"
        },
        "AudioOnlyHlsSettings" : {
          "$ref" : "#/definitions/AudioOnlyHlsSettings"
        }
      }
    },
    "SrtOutputDestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "StreamId" : {
          "type" : "string"
        },
        "EncryptionPassphraseSecretArn" : {
          "type" : "string"
        },
        "Url" : {
          "type" : "string"
        }
      }
    },
    "AutomaticInputFailoverSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ErrorClearTimeMsec" : {
          "type" : "integer"
        },
        "FailoverConditions" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/FailoverCondition"
          }
        },
        "InputPreference" : {
          "type" : "string"
        },
        "SecondaryInputId" : {
          "type" : "string"
        }
      }
    },
    "WavSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CodingMode" : {
          "type" : "string"
        },
        "SampleRate" : {
          "type" : "number"
        },
        "BitDepth" : {
          "type" : "number"
        }
      }
    },
    "M2tsSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "EtvPlatformPid" : {
          "type" : "string"
        },
        "AribCaptionsPid" : {
          "type" : "string"
        },
        "EbpPlacement" : {
          "type" : "string"
        },
        "DvbSubPids" : {
          "type" : "string"
        },
        "SegmentationStyle" : {
          "type" : "string"
        },
        "Klv" : {
          "type" : "string"
        },
        "Scte35PrerollPullupMilliseconds" : {
          "type" : "number"
        },
        "TimedMetadataBehavior" : {
          "type" : "string"
        },
        "DvbTeletextPid" : {
          "type" : "string"
        },
        "Scte35Control" : {
          "type" : "string"
        },
        "PcrPeriod" : {
          "type" : "integer"
        },
        "SegmentationTime" : {
          "type" : "number"
        },
        "CcDescriptor" : {
          "type" : "string"
        },
        "PmtPid" : {
          "type" : "string"
        },
        "DvbNitSettings" : {
          "$ref" : "#/definitions/DvbNitSettings"
        },
        "EtvSignalPid" : {
          "type" : "string"
        },
        "Arib" : {
          "type" : "string"
        },
        "TimedMetadataPid" : {
          "type" : "string"
        },
        "AudioPids" : {
          "type" : "string"
        },
        "AudioBufferModel" : {
          "type" : "string"
        },
        "Ebif" : {
          "type" : "string"
        },
        "PcrControl" : {
          "type" : "string"
        },
        "PatInterval" : {
          "type" : "integer"
        },
        "ProgramNum" : {
          "type" : "integer"
        },
        "RateMode" : {
          "type" : "string"
        },
        "KlvDataPids" : {
          "type" : "string"
        },
        "NullPacketBitrate" : {
          "type" : "number"
        },
        "PmtInterval" : {
          "type" : "integer"
        },
        "EsRateInPes" : {
          "type" : "string"
        },
        "VideoPid" : {
          "type" : "string"
        },
        "TransportStreamId" : {
          "type" : "integer"
        },
        "Scte35Pid" : {
          "type" : "string"
        },
        "AudioStreamType" : {
          "type" : "string"
        },
        "EbpLookaheadMs" : {
          "type" : "integer"
        },
        "DvbTdtSettings" : {
          "$ref" : "#/definitions/DvbTdtSettings"
        },
        "EbpAudioInterval" : {
          "type" : "string"
        },
        "FragmentTime" : {
          "type" : "number"
        },
        "NielsenId3Behavior" : {
          "type" : "string"
        },
        "PcrPid" : {
          "type" : "string"
        },
        "AudioFramesPerPes" : {
          "type" : "integer"
        },
        "AbsentInputAudioBehavior" : {
          "type" : "string"
        },
        "Bitrate" : {
          "type" : "integer"
        },
        "Scte27Pids" : {
          "type" : "string"
        },
        "SegmentationMarkers" : {
          "type" : "string"
        },
        "DvbSdtSettings" : {
          "$ref" : "#/definitions/DvbSdtSettings"
        },
        "BufferModel" : {
          "type" : "string"
        },
        "EcmPid" : {
          "type" : "string"
        },
        "AribCaptionsPidControl" : {
          "type" : "string"
        }
      }
    },
    "DolbyVision81Settings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "HlsGroupSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SegmentationMode" : {
          "type" : "string"
        },
        "Destination" : {
          "$ref" : "#/definitions/OutputLocationRef"
        },
        "CodecSpecification" : {
          "type" : "string"
        },
        "IvSource" : {
          "type" : "string"
        },
        "TimedMetadataId3Frame" : {
          "type" : "string"
        },
        "KeyFormatVersions" : {
          "type" : "string"
        },
        "RedundantManifest" : {
          "type" : "string"
        },
        "OutputSelection" : {
          "type" : "string"
        },
        "KeyProviderSettings" : {
          "$ref" : "#/definitions/KeyProviderSettings"
        },
        "StreamInfResolution" : {
          "type" : "string"
        },
        "CaptionLanguageMappings" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/CaptionLanguageMapping"
          }
        },
        "HlsId3SegmentTagging" : {
          "type" : "string"
        },
        "IFrameOnlyPlaylists" : {
          "type" : "string"
        },
        "CaptionLanguageSetting" : {
          "type" : "string"
        },
        "KeepSegments" : {
          "type" : "integer"
        },
        "ConstantIv" : {
          "type" : "string"
        },
        "DirectoryStructure" : {
          "type" : "string"
        },
        "EncryptionType" : {
          "type" : "string"
        },
        "AdMarkers" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "HlsCdnSettings" : {
          "$ref" : "#/definitions/HlsCdnSettings"
        },
        "IndexNSegments" : {
          "type" : "integer"
        },
        "DiscontinuityTags" : {
          "type" : "string"
        },
        "InputLossAction" : {
          "type" : "string"
        },
        "Mode" : {
          "type" : "string"
        },
        "TsFileMode" : {
          "type" : "string"
        },
        "BaseUrlManifest1" : {
          "type" : "string"
        },
        "ClientCache" : {
          "type" : "string"
        },
        "MinSegmentLength" : {
          "type" : "integer"
        },
        "KeyFormat" : {
          "type" : "string"
        },
        "IvInManifest" : {
          "type" : "string"
        },
        "BaseUrlContent1" : {
          "type" : "string"
        },
        "ProgramDateTimeClock" : {
          "type" : "string"
        },
        "ManifestCompression" : {
          "type" : "string"
        },
        "ManifestDurationFormat" : {
          "type" : "string"
        },
        "TimedMetadataId3Period" : {
          "type" : "integer"
        },
        "IncompleteSegmentBehavior" : {
          "type" : "string"
        },
        "ProgramDateTimePeriod" : {
          "type" : "integer"
        },
        "SegmentLength" : {
          "type" : "integer"
        },
        "TimestampDeltaMilliseconds" : {
          "type" : "integer"
        },
        "ProgramDateTime" : {
          "type" : "string"
        },
        "SegmentsPerSubdirectory" : {
          "type" : "integer"
        },
        "BaseUrlContent" : {
          "type" : "string"
        },
        "BaseUrlManifest" : {
          "type" : "string"
        }
      }
    },
    "FailoverConditionSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AudioSilenceSettings" : {
          "$ref" : "#/definitions/AudioSilenceFailoverSettings"
        },
        "VideoBlackSettings" : {
          "$ref" : "#/definitions/VideoBlackFailoverSettings"
        },
        "InputLossSettings" : {
          "$ref" : "#/definitions/InputLossFailoverSettings"
        }
      }
    },
    "FrameCaptureOutputSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "NameModifier" : {
          "type" : "string"
        }
      }
    },
    "ColorSpacePassthroughSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "ThumbnailConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "State" : {
          "type" : "string"
        }
      }
    },
    "AudioHlsRenditionSelection" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "GroupId" : {
          "type" : "string"
        },
        "Name" : {
          "type" : "string"
        }
      }
    },
    "MsSmoothOutputSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "NameModifier" : {
          "type" : "string"
        },
        "H265PackagingType" : {
          "type" : "string"
        }
      }
    },
    "Scte35SpliceInsert" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AdAvailOffset" : {
          "type" : "integer"
        },
        "WebDeliveryAllowedFlag" : {
          "type" : "string"
        },
        "NoRegionalBlackoutFlag" : {
          "type" : "string"
        }
      }
    },
    "RemixSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ChannelsOut" : {
          "type" : "integer"
        },
        "ChannelsIn" : {
          "type" : "integer"
        },
        "ChannelMappings" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/AudioChannelMapping"
          }
        }
      }
    },
    "ArchiveCdnSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ArchiveS3Settings" : {
          "$ref" : "#/definitions/ArchiveS3Settings"
        }
      }
    },
    "VideoBlackFailoverSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "BlackDetectThreshold" : {
          "type" : "number"
        },
        "VideoBlackThresholdMsec" : {
          "type" : "integer"
        }
      }
    },
    "HlsAkamaiSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Salt" : {
          "type" : "string"
        },
        "FilecacheDuration" : {
          "type" : "integer"
        },
        "NumRetries" : {
          "type" : "integer"
        },
        "Token" : {
          "type" : "string"
        },
        "RestartDelay" : {
          "type" : "integer"
        },
        "ConnectionRetryInterval" : {
          "type" : "integer"
        },
        "HttpTransferMode" : {
          "type" : "string"
        }
      }
    },
    "OutputDestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "StreamName" : {
          "type" : "string"
        },
        "PasswordParam" : {
          "type" : "string"
        },
        "Username" : {
          "type" : "string"
        },
        "Url" : {
          "type" : "string"
        }
      }
    },
    "HlsInputSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Scte35Source" : {
          "type" : "string"
        },
        "BufferSegments" : {
          "type" : "integer"
        },
        "RetryInterval" : {
          "type" : "integer"
        },
        "Retries" : {
          "type" : "integer"
        },
        "Bandwidth" : {
          "type" : "integer"
        }
      }
    },
    "PassThroughSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "Eac3AtmosSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CodingMode" : {
          "type" : "string"
        },
        "Dialnorm" : {
          "type" : "integer"
        },
        "SurroundTrim" : {
          "type" : "number"
        },
        "DrcRf" : {
          "type" : "string"
        },
        "Bitrate" : {
          "type" : "number"
        },
        "DrcLine" : {
          "type" : "string"
        },
        "HeightTrim" : {
          "type" : "number"
        }
      }
    },
    "InputLossFailoverSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "InputLossThresholdMsec" : {
          "type" : "integer"
        }
      }
    },
    "AvailConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Scte35SegmentationScope" : {
          "type" : "string"
        },
        "AvailSettings" : {
          "$ref" : "#/definitions/AvailSettings"
        }
      }
    },
    "AudioSilenceFailoverSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AudioSelectorName" : {
          "type" : "string"
        },
        "AudioSilenceThresholdMsec" : {
          "type" : "integer"
        }
      }
    },
    "RtmpCaptionInfoDestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "AncillarySourceSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SourceAncillaryChannelNumber" : {
          "type" : "integer"
        }
      }
    },
    "EmbeddedPlusScte20DestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "Rec709Settings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "ArchiveContainerSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "M2tsSettings" : {
          "$ref" : "#/definitions/M2tsSettings"
        },
        "RawSettings" : {
          "$ref" : "#/definitions/RawSettings"
        }
      }
    },
    "InputAttachment" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "InputAttachmentName" : {
          "type" : "string"
        },
        "InputId" : {
          "type" : "string"
        },
        "LogicalInterfaceNames" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "AutomaticInputFailoverSettings" : {
          "$ref" : "#/definitions/AutomaticInputFailoverSettings"
        },
        "InputSettings" : {
          "$ref" : "#/definitions/InputSettings"
        }
      }
    },
    "EpochLockingSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "JamSyncTime" : {
          "type" : "string"
        },
        "CustomEpoch" : {
          "type" : "string"
        }
      }
    },
    "VideoSelectorPid" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Pid" : {
          "type" : "integer"
        }
      }
    },
    "InputChannelLevel" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "InputChannel" : {
          "type" : "integer"
        },
        "Gain" : {
          "type" : "integer"
        }
      }
    },
    "MediaPackageOutputSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "Av1ColorSpaceSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Rec601Settings" : {
          "$ref" : "#/definitions/Rec601Settings"
        },
        "Rec709Settings" : {
          "$ref" : "#/definitions/Rec709Settings"
        },
        "ColorSpacePassthroughSettings" : {
          "$ref" : "#/definitions/ColorSpacePassthroughSettings"
        },
        "Hdr10Settings" : {
          "$ref" : "#/definitions/Hdr10Settings"
        }
      }
    },
    "HlsWebdavSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FilecacheDuration" : {
          "type" : "integer"
        },
        "RestartDelay" : {
          "type" : "integer"
        },
        "NumRetries" : {
          "type" : "integer"
        },
        "ConnectionRetryInterval" : {
          "type" : "integer"
        },
        "HttpTransferMode" : {
          "type" : "string"
        }
      }
    },
    "TemporalFilterSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "PostFilterSharpening" : {
          "type" : "string"
        },
        "Strength" : {
          "type" : "string"
        }
      }
    },
    "Mp2Settings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CodingMode" : {
          "type" : "string"
        },
        "SampleRate" : {
          "type" : "number"
        },
        "Bitrate" : {
          "type" : "number"
        }
      }
    },
    "OutputSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MediaPackageOutputSettings" : {
          "$ref" : "#/definitions/MediaPackageOutputSettings"
        },
        "MsSmoothOutputSettings" : {
          "$ref" : "#/definitions/MsSmoothOutputSettings"
        },
        "FrameCaptureOutputSettings" : {
          "$ref" : "#/definitions/FrameCaptureOutputSettings"
        },
        "HlsOutputSettings" : {
          "$ref" : "#/definitions/HlsOutputSettings"
        },
        "RtmpOutputSettings" : {
          "$ref" : "#/definitions/RtmpOutputSettings"
        },
        "UdpOutputSettings" : {
          "$ref" : "#/definitions/UdpOutputSettings"
        },
        "MultiplexOutputSettings" : {
          "$ref" : "#/definitions/MultiplexOutputSettings"
        },
        "CmafIngestOutputSettings" : {
          "$ref" : "#/definitions/CmafIngestOutputSettings"
        },
        "SrtOutputSettings" : {
          "$ref" : "#/definitions/SrtOutputSettings"
        },
        "ArchiveOutputSettings" : {
          "$ref" : "#/definitions/ArchiveOutputSettings"
        }
      }
    },
    "RtmpOutputSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Destination" : {
          "$ref" : "#/definitions/OutputLocationRef"
        },
        "CertificateMode" : {
          "type" : "string"
        },
        "NumRetries" : {
          "type" : "integer"
        },
        "ConnectionRetryInterval" : {
          "type" : "integer"
        }
      }
    },
    "CaptionDestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AribDestinationSettings" : {
          "$ref" : "#/definitions/AribDestinationSettings"
        },
        "EbuTtDDestinationSettings" : {
          "$ref" : "#/definitions/EbuTtDDestinationSettings"
        },
        "SmpteTtDestinationSettings" : {
          "$ref" : "#/definitions/SmpteTtDestinationSettings"
        },
        "EmbeddedPlusScte20DestinationSettings" : {
          "$ref" : "#/definitions/EmbeddedPlusScte20DestinationSettings"
        },
        "TtmlDestinationSettings" : {
          "$ref" : "#/definitions/TtmlDestinationSettings"
        },
        "Scte20PlusEmbeddedDestinationSettings" : {
          "$ref" : "#/definitions/Scte20PlusEmbeddedDestinationSettings"
        },
        "DvbSubDestinationSettings" : {
          "$ref" : "#/definitions/DvbSubDestinationSettings"
        },
        "TeletextDestinationSettings" : {
          "$ref" : "#/definitions/TeletextDestinationSettings"
        },
        "BurnInDestinationSettings" : {
          "$ref" : "#/definitions/BurnInDestinationSettings"
        },
        "WebvttDestinationSettings" : {
          "$ref" : "#/definitions/WebvttDestinationSettings"
        },
        "EmbeddedDestinationSettings" : {
          "$ref" : "#/definitions/EmbeddedDestinationSettings"
        },
        "RtmpCaptionInfoDestinationSettings" : {
          "$ref" : "#/definitions/RtmpCaptionInfoDestinationSettings"
        },
        "Scte27DestinationSettings" : {
          "$ref" : "#/definitions/Scte27DestinationSettings"
        }
      }
    },
    "AudioTrack" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Track" : {
          "type" : "integer"
        }
      }
    },
    "Scte20SourceSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Source608ChannelNumber" : {
          "type" : "integer"
        },
        "Convert608To708" : {
          "type" : "string"
        }
      }
    },
    "Scte27DestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "Eac3Settings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CodingMode" : {
          "type" : "string"
        },
        "SurroundMode" : {
          "type" : "string"
        },
        "PassthroughControl" : {
          "type" : "string"
        },
        "Dialnorm" : {
          "type" : "integer"
        },
        "LoRoSurroundMixLevel" : {
          "type" : "number"
        },
        "PhaseControl" : {
          "type" : "string"
        },
        "LtRtCenterMixLevel" : {
          "type" : "number"
        },
        "LfeFilter" : {
          "type" : "string"
        },
        "LfeControl" : {
          "type" : "string"
        },
        "Bitrate" : {
          "type" : "number"
        },
        "DrcLine" : {
          "type" : "string"
        },
        "DcFilter" : {
          "type" : "string"
        },
        "MetadataControl" : {
          "type" : "string"
        },
        "LtRtSurroundMixLevel" : {
          "type" : "number"
        },
        "LoRoCenterMixLevel" : {
          "type" : "number"
        },
        "DrcRf" : {
          "type" : "string"
        },
        "AttenuationControl" : {
          "type" : "string"
        },
        "BitstreamMode" : {
          "type" : "string"
        },
        "SurroundExMode" : {
          "type" : "string"
        },
        "StereoDownmix" : {
          "type" : "string"
        }
      }
    },
    "InputSpecification" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Codec" : {
          "type" : "string"
        },
        "MaximumBitrate" : {
          "type" : "string"
        },
        "Resolution" : {
          "type" : "string"
        }
      }
    },
    "TimecodeBurninSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Prefix" : {
          "type" : "string"
        },
        "FontSize" : {
          "type" : "string"
        },
        "Position" : {
          "type" : "string"
        }
      }
    },
    "AudioSelector" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SelectorSettings" : {
          "$ref" : "#/definitions/AudioSelectorSettings"
        },
        "Name" : {
          "type" : "string"
        }
      }
    },
    "HlsS3Settings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CannedAcl" : {
          "type" : "string"
        }
      }
    },
    "MotionGraphicsSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "HtmlMotionGraphicsSettings" : {
          "$ref" : "#/definitions/HtmlMotionGraphicsSettings"
        }
      }
    },
    "TtmlDestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "StyleControl" : {
          "type" : "string"
        }
      }
    },
    "MultiplexProgramChannelDestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ProgramName" : {
          "type" : "string"
        },
        "MultiplexId" : {
          "type" : "string"
        }
      }
    },
    "H265Settings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MvOverPictureBoundaries" : {
          "type" : "string"
        },
        "TimecodeBurninSettings" : {
          "$ref" : "#/definitions/TimecodeBurninSettings"
        },
        "Slices" : {
          "type" : "integer"
        },
        "QvbrQualityLevel" : {
          "type" : "integer"
        },
        "TileHeight" : {
          "type" : "integer"
        },
        "FramerateNumerator" : {
          "type" : "integer"
        },
        "GopClosedCadence" : {
          "type" : "integer"
        },
        "FlickerAq" : {
          "type" : "string"
        },
        "Profile" : {
          "type" : "string"
        },
        "MvTemporalPredictor" : {
          "type" : "string"
        },
        "MinIInterval" : {
          "type" : "integer"
        },
        "SceneChangeDetect" : {
          "type" : "string"
        },
        "FramerateDenominator" : {
          "type" : "integer"
        },
        "GopSize" : {
          "type" : "number"
        },
        "AdaptiveQuantization" : {
          "type" : "string"
        },
        "TileWidth" : {
          "type" : "integer"
        },
        "FilterSettings" : {
          "$ref" : "#/definitions/H265FilterSettings"
        },
        "MinQp" : {
          "type" : "integer"
        },
        "AlternativeTransferFunction" : {
          "type" : "string"
        },
        "ColorSpaceSettings" : {
          "$ref" : "#/definitions/H265ColorSpaceSettings"
        },
        "Tier" : {
          "type" : "string"
        },
        "ParDenominator" : {
          "type" : "integer"
        },
        "FixedAfd" : {
          "type" : "string"
        },
        "GopSizeUnits" : {
          "type" : "string"
        },
        "TilePadding" : {
          "type" : "string"
        },
        "AfdSignaling" : {
          "type" : "string"
        },
        "Bitrate" : {
          "type" : "integer"
        },
        "ParNumerator" : {
          "type" : "integer"
        },
        "RateControlMode" : {
          "type" : "string"
        },
        "ScanType" : {
          "type" : "string"
        },
        "BufSize" : {
          "type" : "integer"
        },
        "TimecodeInsertion" : {
          "type" : "string"
        },
        "Deblocking" : {
          "type" : "string"
        },
        "ColorMetadata" : {
          "type" : "string"
        },
        "LookAheadRateControl" : {
          "type" : "string"
        },
        "Level" : {
          "type" : "string"
        },
        "MaxBitrate" : {
          "type" : "integer"
        },
        "TreeblockSize" : {
          "type" : "string"
        }
      }
    },
    "HlsBasicPutSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FilecacheDuration" : {
          "type" : "integer"
        },
        "RestartDelay" : {
          "type" : "integer"
        },
        "NumRetries" : {
          "type" : "integer"
        },
        "ConnectionRetryInterval" : {
          "type" : "integer"
        }
      }
    },
    "H264ColorSpaceSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Rec601Settings" : {
          "$ref" : "#/definitions/Rec601Settings"
        },
        "Rec709Settings" : {
          "$ref" : "#/definitions/Rec709Settings"
        },
        "ColorSpacePassthroughSettings" : {
          "$ref" : "#/definitions/ColorSpacePassthroughSettings"
        }
      }
    },
    "AudioNormalizationSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TargetLkfs" : {
          "type" : "number"
        },
        "Algorithm" : {
          "type" : "string"
        },
        "AlgorithmControl" : {
          "type" : "string"
        }
      }
    },
    "DvbSubDestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "BackgroundOpacity" : {
          "type" : "integer"
        },
        "FontResolution" : {
          "type" : "integer"
        },
        "OutlineColor" : {
          "type" : "string"
        },
        "FontColor" : {
          "type" : "string"
        },
        "ShadowColor" : {
          "type" : "string"
        },
        "ShadowOpacity" : {
          "type" : "integer"
        },
        "Font" : {
          "$ref" : "#/definitions/InputLocation"
        },
        "ShadowYOffset" : {
          "type" : "integer"
        },
        "Alignment" : {
          "type" : "string"
        },
        "XPosition" : {
          "type" : "integer"
        },
        "FontSize" : {
          "type" : "string"
        },
        "YPosition" : {
          "type" : "integer"
        },
        "OutlineSize" : {
          "type" : "integer"
        },
        "TeletextGridControl" : {
          "type" : "string"
        },
        "FontOpacity" : {
          "type" : "integer"
        },
        "ShadowXOffset" : {
          "type" : "integer"
        },
        "BackgroundColor" : {
          "type" : "string"
        }
      }
    },
    "OutputLockingSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "EpochLockingSettings" : {
          "$ref" : "#/definitions/EpochLockingSettings"
        },
        "PipelineLockingSettings" : {
          "$ref" : "#/definitions/PipelineLockingSettings"
        }
      }
    },
    "CaptionDescription" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DestinationSettings" : {
          "$ref" : "#/definitions/CaptionDestinationSettings"
        },
        "LanguageCode" : {
          "type" : "string"
        },
        "LanguageDescription" : {
          "type" : "string"
        },
        "Accessibility" : {
          "type" : "string"
        },
        "DvbDashAccessibility" : {
          "type" : "string"
        },
        "CaptionSelectorName" : {
          "type" : "string"
        },
        "CaptionDashRoles" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "Name" : {
          "type" : "string"
        }
      }
    },
    "BurnInDestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "BackgroundOpacity" : {
          "type" : "integer"
        },
        "FontResolution" : {
          "type" : "integer"
        },
        "OutlineColor" : {
          "type" : "string"
        },
        "FontColor" : {
          "type" : "string"
        },
        "ShadowColor" : {
          "type" : "string"
        },
        "ShadowOpacity" : {
          "type" : "integer"
        },
        "Font" : {
          "$ref" : "#/definitions/InputLocation"
        },
        "ShadowYOffset" : {
          "type" : "integer"
        },
        "Alignment" : {
          "type" : "string"
        },
        "XPosition" : {
          "type" : "integer"
        },
        "FontSize" : {
          "type" : "string"
        },
        "YPosition" : {
          "type" : "integer"
        },
        "OutlineSize" : {
          "type" : "integer"
        },
        "TeletextGridControl" : {
          "type" : "string"
        },
        "FontOpacity" : {
          "type" : "integer"
        },
        "ShadowXOffset" : {
          "type" : "integer"
        },
        "BackgroundColor" : {
          "type" : "string"
        }
      }
    },
    "Mpeg2Settings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TimecodeBurninSettings" : {
          "$ref" : "#/definitions/TimecodeBurninSettings"
        },
        "ColorSpace" : {
          "type" : "string"
        },
        "FixedAfd" : {
          "type" : "string"
        },
        "GopSizeUnits" : {
          "type" : "string"
        },
        "FramerateNumerator" : {
          "type" : "integer"
        },
        "GopClosedCadence" : {
          "type" : "integer"
        },
        "AfdSignaling" : {
          "type" : "string"
        },
        "DisplayAspectRatio" : {
          "type" : "string"
        },
        "ScanType" : {
          "type" : "string"
        },
        "TimecodeInsertion" : {
          "type" : "string"
        },
        "ColorMetadata" : {
          "type" : "string"
        },
        "FramerateDenominator" : {
          "type" : "integer"
        },
        "GopSize" : {
          "type" : "number"
        },
        "AdaptiveQuantization" : {
          "type" : "string"
        },
        "SubgopLength" : {
          "type" : "string"
        },
        "FilterSettings" : {
          "$ref" : "#/definitions/Mpeg2FilterSettings"
        },
        "GopNumBFrames" : {
          "type" : "integer"
        }
      }
    },
    "HtmlMotionGraphicsSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "MultiplexOutputSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Destination" : {
          "$ref" : "#/definitions/OutputLocationRef"
        },
        "ContainerSettings" : {
          "$ref" : "#/definitions/MultiplexContainerSettings"
        }
      }
    },
    "AudioOnlyHlsSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SegmentType" : {
          "type" : "string"
        },
        "AudioTrackType" : {
          "type" : "string"
        },
        "AudioGroupId" : {
          "type" : "string"
        },
        "AudioOnlyImage" : {
          "$ref" : "#/definitions/InputLocation"
        }
      }
    },
    "StaticKeySettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "KeyProviderServer" : {
          "$ref" : "#/definitions/InputLocation"
        },
        "StaticKeyValue" : {
          "type" : "string"
        }
      }
    },
    "EmbeddedSourceSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Source608ChannelNumber" : {
          "type" : "integer"
        },
        "Scte20Detection" : {
          "type" : "string"
        },
        "Source608TrackNumber" : {
          "type" : "integer"
        },
        "Convert608To708" : {
          "type" : "string"
        }
      }
    },
    "CaptionRectangle" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Height" : {
          "type" : "number"
        },
        "TopOffset" : {
          "type" : "number"
        },
        "Width" : {
          "type" : "number"
        },
        "LeftOffset" : {
          "type" : "number"
        }
      }
    },
    "Av1Settings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TimecodeBurninSettings" : {
          "$ref" : "#/definitions/TimecodeBurninSettings"
        },
        "ColorSpaceSettings" : {
          "$ref" : "#/definitions/Av1ColorSpaceSettings"
        },
        "QvbrQualityLevel" : {
          "type" : "integer"
        },
        "ParDenominator" : {
          "type" : "integer"
        },
        "FixedAfd" : {
          "type" : "string"
        },
        "GopSizeUnits" : {
          "type" : "string"
        },
        "FramerateNumerator" : {
          "type" : "integer"
        },
        "AfdSignaling" : {
          "type" : "string"
        },
        "ParNumerator" : {
          "type" : "integer"
        },
        "BufSize" : {
          "type" : "integer"
        },
        "MinIInterval" : {
          "type" : "integer"
        },
        "SceneChangeDetect" : {
          "type" : "string"
        },
        "FramerateDenominator" : {
          "type" : "integer"
        },
        "LookAheadRateControl" : {
          "type" : "string"
        },
        "Level" : {
          "type" : "string"
        },
        "MaxBitrate" : {
          "type" : "integer"
        },
        "GopSize" : {
          "type" : "number"
        }
      }
    },
    "TimecodeConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SyncThreshold" : {
          "type" : "integer"
        },
        "Source" : {
          "type" : "string"
        }
      }
    },
    "AacSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CodingMode" : {
          "type" : "string"
        },
        "RateControlMode" : {
          "type" : "string"
        },
        "SampleRate" : {
          "type" : "number"
        },
        "InputType" : {
          "type" : "string"
        },
        "VbrQuality" : {
          "type" : "string"
        },
        "RawFormat" : {
          "type" : "string"
        },
        "Spec" : {
          "type" : "string"
        },
        "Bitrate" : {
          "type" : "number"
        },
        "Profile" : {
          "type" : "string"
        }
      }
    },
    "ArchiveOutputSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Extension" : {
          "type" : "string"
        },
        "NameModifier" : {
          "type" : "string"
        },
        "ContainerSettings" : {
          "$ref" : "#/definitions/ArchiveContainerSettings"
        }
      }
    },
    "VpcOutputSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SecurityGroupIds" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "SubnetIds" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "PublicAddressAllocationIds" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        }
      }
    },
    "AudioWatermarkSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "NielsenWatermarksSettings" : {
          "$ref" : "#/definitions/NielsenWatermarksSettings"
        }
      }
    },
    "EbuTtDDestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FontFamily" : {
          "type" : "string"
        },
        "StyleControl" : {
          "type" : "string"
        },
        "CopyrightHolder" : {
          "type" : "string"
        },
        "FillLineGap" : {
          "type" : "string"
        }
      }
    },
    "HlsCdnSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "HlsWebdavSettings" : {
          "$ref" : "#/definitions/HlsWebdavSettings"
        },
        "HlsS3Settings" : {
          "$ref" : "#/definitions/HlsS3Settings"
        },
        "HlsBasicPutSettings" : {
          "$ref" : "#/definitions/HlsBasicPutSettings"
        },
        "HlsMediaStoreSettings" : {
          "$ref" : "#/definitions/HlsMediaStoreSettings"
        },
        "HlsAkamaiSettings" : {
          "$ref" : "#/definitions/HlsAkamaiSettings"
        }
      }
    },
    "VideoSelector" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ColorSpaceSettings" : {
          "$ref" : "#/definitions/VideoSelectorColorSpaceSettings"
        },
        "ColorSpaceUsage" : {
          "type" : "string"
        },
        "SelectorSettings" : {
          "$ref" : "#/definitions/VideoSelectorSettings"
        },
        "ColorSpace" : {
          "type" : "string"
        }
      }
    },
    "MotionGraphicsConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MotionGraphicsSettings" : {
          "$ref" : "#/definitions/MotionGraphicsSettings"
        },
        "MotionGraphicsInsertion" : {
          "type" : "string"
        }
      }
    },
    "Hdr10Settings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MaxCll" : {
          "type" : "integer"
        },
        "MaxFall" : {
          "type" : "integer"
        }
      }
    },
    "CaptionSelector" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "LanguageCode" : {
          "type" : "string"
        },
        "SelectorSettings" : {
          "$ref" : "#/definitions/CaptionSelectorSettings"
        },
        "Name" : {
          "type" : "string"
        }
      }
    },
    "Scte35TimeSignalApos" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AdAvailOffset" : {
          "type" : "integer"
        },
        "WebDeliveryAllowedFlag" : {
          "type" : "string"
        },
        "NoRegionalBlackoutFlag" : {
          "type" : "string"
        }
      }
    },
    "DvbSdtSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ServiceProviderName" : {
          "type" : "string"
        },
        "OutputSdt" : {
          "type" : "string"
        },
        "ServiceName" : {
          "type" : "string"
        },
        "RepInterval" : {
          "type" : "integer"
        }
      }
    },
    "NielsenWatermarksSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "NielsenNaesIiNwSettings" : {
          "$ref" : "#/definitions/NielsenNaesIiNw"
        },
        "NielsenDistributionType" : {
          "type" : "string"
        },
        "NielsenCbetSettings" : {
          "$ref" : "#/definitions/NielsenCBET"
        }
      }
    },
    "MsSmoothGroupSettings" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SegmentationMode" : {
          "type" : "string"
        },
        "Destination" : {
          "$ref" : "#/definitions/OutputLocationRef"
        },
        "EventStopBehavior" : {
          "type" : "string"
        },
        "FilecacheDuration" : {
          "type" : "integer"
        },
        "CertificateMode" : {
          "type" : "string"
        },
        "AcquisitionPointId" : {
          "type" : "string"
        },
        "StreamManifestBehavior" : {
          "type" : "string"
        },
        "InputLossAction" : {
          "type" : "string"
        },
        "FragmentLength" : {
          "type" : "integer"
        },
        "RestartDelay" : {
          "type" : "integer"
        },
        "SparseTrackType" : {
          "type" : "string"
        },
        "EventIdMode" : {
          "type" : "string"
        },
        "TimestampOffsetMode" : {
          "type" : "string"
        },
        "AudioOnlyTimecodeControl" : {
          "type" : "string"
        },
        "NumRetries" : {
          "type" : "integer"
        },
        "TimestampOffset" : {
          "type" : "string"
        },
        "EventId" : {
          "type" : "string"
        },
        "SendDelayMs" : {
          "type" : "integer"
        },
        "ConnectionRetryInterval" : {
          "type" : "integer"
        }
      }
    },
    "EmbeddedDestinationSettings" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "OutputLocationRef" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DestinationRefId" : {
          "type" : "string"
        }
      }
    },
    "NielsenNaesIiNw" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Timezone" : {
          "type" : "string"
        },
        "CheckDigitString" : {
          "type" : "string"
        },
        "Sid" : {
          "type" : "number"
        }
      }
    }
  },
  "createOnlyProperties" : [ "/properties/Vpc", "/properties/AnywhereSettings" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Inputs", "/properties/Id", "/properties/Arn" ]
}