SCHEMA = {
  "typeName" : "AWS::MediaLive::Multiplexprogram",
  "description" : "Resource schema for AWS::MediaLive::Multiplexprogram",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-medialiveprogram.git",
  "properties" : {
    "ChannelId" : {
      "type" : "string",
      "description" : "The MediaLive channel associated with the program."
    },
    "MultiplexId" : {
      "type" : "string",
      "description" : "The ID of the multiplex that the program belongs to."
    },
    "MultiplexProgramSettings" : {
      "description" : "The settings for this multiplex program.",
      "$ref" : "#/definitions/MultiplexProgramSettings"
    },
    "PreferredChannelPipeline" : {
      "description" : "The settings for this multiplex program.",
      "$ref" : "#/definitions/PreferredChannelPipeline"
    },
    "PacketIdentifiersMap" : {
      "$ref" : "#/definitions/MultiplexProgramPacketIdentifiersMap",
      "description" : "The packet identifier map for this multiplex program."
    },
    "PipelineDetails" : {
      "description" : "Contains information about the current sources for the specified program in the specified multiplex. Keep in mind that each multiplex pipeline connects to both pipelines in a given source channel (the channel identified by the program). But only one of those channel pipelines is ever active at one time.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/MultiplexProgramPipelineDetail"
      },
      "insertionOrder" : True
    },
    "ProgramName" : {
      "type" : "string",
      "description" : "The name of the multiplex program."
    }
  },
  "definitions" : {
    "MultiplexProgramSettings" : {
      "description" : "Multiplex Program settings configuration.",
      "type" : "object",
      "properties" : {
        "PreferredChannelPipeline" : {
          "type" : "string",
          "$ref" : "#/definitions/PreferredChannelPipeline"
        },
        "ProgramNumber" : {
          "type" : "integer",
          "description" : "Unique program number.",
          "minimum" : 0,
          "maximum" : 65535
        },
        "ServiceDescriptor" : {
          "$ref" : "#/definitions/MultiplexProgramServiceDescriptor",
          "description" : "Transport stream service descriptor configuration for the Multiplex program."
        },
        "VideoSettings" : {
          "$ref" : "#/definitions/MultiplexVideoSettings",
          "description" : "Program video settings configuration."
        }
      },
      "required" : [ "ProgramNumber" ],
      "additionalProperties" : False
    },
    "PreferredChannelPipeline" : {
      "type" : "string",
      "description" : "Indicates which pipeline is preferred by the multiplex for program ingest.\nIf set to \\\"PIPELINE_0\\\" or \\\"PIPELINE_1\\\" and an unhealthy ingest causes the multiplex to switch to the non-preferred pipeline,\nit will switch back once that ingest is healthy again. If set to \\\"CURRENTLY_ACTIVE\\\",\nit will not switch back to the other pipeline based on it recovering to a healthy state,\nit will only switch if the active pipeline becomes unhealthy.\n",
      "enum" : [ "CURRENTLY_ACTIVE", "PIPELINE_0", "PIPELINE_1" ]
    },
    "MultiplexProgramServiceDescriptor" : {
      "description" : "Transport stream service descriptor configuration for the Multiplex program.",
      "type" : "object",
      "properties" : {
        "ProviderName" : {
          "type" : "string",
          "description" : "Name of the provider.",
          "minLength" : 1,
          "maxLength" : 256
        },
        "ServiceName" : {
          "type" : "string",
          "description" : "Name of the service.",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "required" : [ "ProviderName", "ServiceName" ],
      "additionalProperties" : False
    },
    "MultiplexVideoSettings" : {
      "description" : "The video configuration for each program in a multiplex.",
      "type" : "object",
      "oneOf" : [ {
        "type" : "object",
        "properties" : {
          "ConstantBitrate" : {
            "type" : "integer",
            "description" : "The constant bitrate configuration for the video encode.\nWhen this field is defined, StatmuxSettings must be undefined.",
            "minimum" : 100000,
            "maximum" : 100000000
          }
        },
        "required" : [ "ConstantBitrate" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "properties" : {
          "StatmuxSettings" : {
            "description" : "Statmux rate control settings.\nWhen this field is defined, ConstantBitrate must be undefined.",
            "$ref" : "#/definitions/MultiplexStatmuxVideoSettings"
          }
        },
        "required" : [ "StatmuxSettings" ],
        "additionalProperties" : False
      } ]
    },
    "MultiplexStatmuxVideoSettings" : {
      "description" : "Statmux rate control settings",
      "type" : "object",
      "properties" : {
        "MaximumBitrate" : {
          "type" : "integer",
          "description" : "Maximum statmux bitrate.",
          "minimum" : 100000,
          "maximum" : 100000000
        },
        "MinimumBitrate" : {
          "type" : "integer",
          "description" : "Minimum statmux bitrate.",
          "minimum" : 100000,
          "maximum" : 100000000
        },
        "Priority" : {
          "type" : "integer",
          "description" : "The purpose of the priority is to use a combination of the\\nmultiplex rate control algorithm and the QVBR capability of the\\nencoder to prioritize the video quality of some channels in a\\nmultiplex over others.  Channels that have a higher priority will\\nget higher video quality at the expense of the video quality of\\nother channels in the multiplex with lower priority.",
          "minimum" : -5,
          "maximum" : 5
        }
      },
      "additionalProperties" : False
    },
    "MultiplexProgramPacketIdentifiersMap" : {
      "description" : "Packet identifiers map for a given Multiplex program.",
      "type" : "object",
      "properties" : {
        "AudioPids" : {
          "type" : "array",
          "items" : {
            "type" : "integer"
          },
          "insertionOrder" : True
        },
        "DvbSubPids" : {
          "type" : "array",
          "items" : {
            "type" : "integer"
          },
          "insertionOrder" : True
        },
        "DvbTeletextPid" : {
          "type" : "integer"
        },
        "EtvPlatformPid" : {
          "type" : "integer"
        },
        "EtvSignalPid" : {
          "type" : "integer"
        },
        "KlvDataPids" : {
          "type" : "array",
          "items" : {
            "type" : "integer"
          },
          "insertionOrder" : True
        },
        "PcrPid" : {
          "type" : "integer"
        },
        "PmtPid" : {
          "type" : "integer"
        },
        "PrivateMetadataPid" : {
          "type" : "integer"
        },
        "Scte27Pids" : {
          "type" : "array",
          "items" : {
            "type" : "integer"
          },
          "insertionOrder" : True
        },
        "Scte35Pid" : {
          "type" : "integer"
        },
        "TimedMetadataPid" : {
          "type" : "integer"
        },
        "VideoPid" : {
          "type" : "integer"
        }
      },
      "additionalProperties" : False
    },
    "MultiplexProgramPipelineDetail" : {
      "description" : "The current source for one of the pipelines in the multiplex.",
      "type" : "object",
      "properties" : {
        "ActiveChannelPipeline" : {
          "type" : "string",
          "description" : "Identifies the channel pipeline that is currently active for the pipeline (identified by PipelineId) in the multiplex."
        },
        "PipelineId" : {
          "type" : "string",
          "description" : "Identifies a specific pipeline in the multiplex."
        }
      },
      "additionalProperties" : False
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/ProgramName", "/properties/MultiplexId" ],
  "readOnlyProperties" : [ "/properties/ChannelId" ],
  "writeOnlyProperties" : [ "/properties/PreferredChannelPipeline" ],
  "createOnlyProperties" : [ "/properties/ProgramName", "/properties/MultiplexId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "medialive:CreateMultiplexProgram", "medialive:DescribeMultiplexProgram" ]
    },
    "read" : {
      "permissions" : [ "medialive:DescribeMultiplexProgram" ]
    },
    "update" : {
      "permissions" : [ "medialive:UpdateMultiplexProgram", "medialive:DescribeMultiplexProgram" ]
    },
    "delete" : {
      "permissions" : [ "medialive:DeleteMultiplexProgram", "medialive:DescribeMultiplexProgram" ]
    },
    "list" : {
      "permissions" : [ "medialive:ListMultiplexPrograms" ],
      "handlerSchema" : {
        "properties" : {
          "Arn" : {
            "$ref" : "resource-schema.json#/properties/MultiplexId"
          }
        },
        "required" : [ "MultiplexId" ]
      }
    }
  },
  "tagging" : {
    "taggable" : False
  }
}