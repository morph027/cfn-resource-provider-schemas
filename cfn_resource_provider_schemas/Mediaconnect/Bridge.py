SCHEMA = {
  "typeName" : "AWS::MediaConnect::Bridge",
  "description" : "Resource schema for AWS::MediaConnect::Bridge",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-mediaconnect.git",
  "definitions" : {
    "FailoverConfig" : {
      "description" : "The settings for source failover.",
      "type" : "object",
      "properties" : {
        "State" : {
          "$ref" : "#/definitions/FailoverConfigStateEnum"
        },
        "FailoverMode" : {
          "description" : "The type of failover you choose for this flow. FAILOVER allows switching between different streams.",
          "$ref" : "#/definitions/FailoverModeEnum"
        },
        "SourcePriority" : {
          "description" : "The priority you want to assign to a source. You can have a primary stream and a backup stream or two equally prioritized streams.",
          "$ref" : "#/definitions/SourcePriority"
        }
      },
      "required" : [ "FailoverMode" ],
      "additionalProperties" : False
    },
    "BridgeStateEnum" : {
      "type" : "string",
      "enum" : [ "CREATING", "STANDBY", "STARTING", "DEPLOYING", "ACTIVE", "STOPPING", "DELETING", "DELETED", "START_FAILED", "START_PENDING", "UPDATING" ]
    },
    "FailoverConfigStateEnum" : {
      "type" : "string",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "FailoverModeEnum" : {
      "type" : "string",
      "enum" : [ "FAILOVER" ]
    },
    "SourcePriority" : {
      "type" : "object",
      "description" : "The priority you want to assign to a source. You can have a primary stream and a backup stream or two equally prioritized streams.",
      "properties" : {
        "PrimarySource" : {
          "description" : "The name of the source you choose as the primary source for this flow.",
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "BridgeOutput" : {
      "description" : "The output of the bridge.",
      "type" : "object",
      "properties" : {
        "NetworkOutput" : {
          "$ref" : "#/definitions/BridgeNetworkOutput"
        }
      },
      "additionalProperties" : False
    },
    "BridgeNetworkOutput" : {
      "description" : "The output of the bridge. A network output is delivered to your premises.",
      "type" : "object",
      "properties" : {
        "Name" : {
          "description" : "The network output name.",
          "type" : "string"
        },
        "Protocol" : {
          "description" : "The network output protocol.",
          "$ref" : "#/definitions/ProtocolEnum"
        },
        "IpAddress" : {
          "description" : "The network output IP Address.",
          "type" : "string"
        },
        "Port" : {
          "description" : "The network output port.",
          "type" : "integer"
        },
        "NetworkName" : {
          "description" : "The network output's gateway network name.",
          "type" : "string"
        },
        "Ttl" : {
          "description" : "The network output TTL.",
          "type" : "integer"
        }
      },
      "additionalProperties" : False,
      "required" : [ "Name", "Protocol", "IpAddress", "Port", "NetworkName", "Ttl" ]
    },
    "BridgeSource" : {
      "description" : "The bridge's source.",
      "type" : "object",
      "properties" : {
        "FlowSource" : {
          "$ref" : "#/definitions/BridgeFlowSource"
        },
        "NetworkSource" : {
          "$ref" : "#/definitions/BridgeNetworkSource"
        }
      },
      "additionalProperties" : False
    },
    "BridgeFlowSource" : {
      "type" : "object",
      "description" : "The source of the bridge. A flow source originates in MediaConnect as an existing cloud flow.",
      "properties" : {
        "Name" : {
          "description" : "The name of the flow source.",
          "type" : "string"
        },
        "FlowArn" : {
          "description" : "The ARN of the cloud flow used as a source of this bridge.",
          "type" : "string"
        },
        "FlowVpcInterfaceAttachment" : {
          "description" : "The name of the VPC interface attachment to use for this source.",
          "$ref" : "#/definitions/VpcInterfaceAttachment"
        }
      },
      "additionalProperties" : False,
      "required" : [ "Name", "FlowArn" ]
    },
    "VpcInterfaceAttachment" : {
      "type" : "object",
      "description" : "The settings for attaching a VPC interface to an resource.",
      "properties" : {
        "VpcInterfaceName" : {
          "description" : "The name of the VPC interface to use for this resource.",
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "BridgeNetworkSource" : {
      "type" : "object",
      "description" : "The source of the bridge. A network source originates at your premises.",
      "properties" : {
        "Name" : {
          "description" : "The name of the network source.",
          "type" : "string"
        },
        "Protocol" : {
          "description" : "The network source protocol.",
          "$ref" : "#/definitions/ProtocolEnum"
        },
        "MulticastIp" : {
          "description" : "The network source multicast IP.",
          "type" : "string"
        },
        "MulticastSourceSettings" : {
          "description" : "The settings related to the multicast source.",
          "$ref" : "#/definitions/MulticastSourceSettings"
        },
        "Port" : {
          "description" : "The network source port.",
          "type" : "integer"
        },
        "NetworkName" : {
          "description" : "The network source's gateway network name.",
          "type" : "string"
        }
      },
      "required" : [ "Name", "Protocol", "MulticastIp", "Port", "NetworkName" ],
      "additionalProperties" : False
    },
    "MulticastSourceSettings" : {
      "type" : "object",
      "description" : "The settings related to the multicast source.",
      "properties" : {
        "MulticastSourceIp" : {
          "description" : "The IP address of the source for source-specific multicast (SSM).",
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "ProtocolEnum" : {
      "type" : "string",
      "enum" : [ "rtp-fec", "rtp", "udp" ]
    },
    "IngressGatewayBridge" : {
      "type" : "object",
      "properties" : {
        "MaxBitrate" : {
          "description" : "The maximum expected bitrate of the ingress bridge.",
          "type" : "integer"
        },
        "MaxOutputs" : {
          "description" : "The maximum number of outputs on the ingress bridge.",
          "type" : "integer"
        }
      },
      "additionalProperties" : False,
      "required" : [ "MaxBitrate", "MaxOutputs" ]
    },
    "EgressGatewayBridge" : {
      "type" : "object",
      "properties" : {
        "MaxBitrate" : {
          "type" : "integer",
          "description" : "The maximum expected bitrate of the egress bridge."
        }
      },
      "additionalProperties" : False,
      "required" : [ "MaxBitrate" ]
    }
  },
  "properties" : {
    "Name" : {
      "description" : "The name of the bridge.",
      "type" : "string"
    },
    "BridgeArn" : {
      "description" : "The Amazon Resource Number (ARN) of the bridge.",
      "type" : "string"
    },
    "PlacementArn" : {
      "description" : "The placement Amazon Resource Number (ARN) of the bridge.",
      "type" : "string"
    },
    "BridgeState" : {
      "$ref" : "#/definitions/BridgeStateEnum"
    },
    "SourceFailoverConfig" : {
      "$ref" : "#/definitions/FailoverConfig"
    },
    "Outputs" : {
      "description" : "The outputs on this bridge.",
      "type" : "array",
      "minItems" : 0,
      "maxItems" : 2,
      "items" : {
        "$ref" : "#/definitions/BridgeOutput"
      },
      "insertionOrder" : True
    },
    "Sources" : {
      "description" : "The sources on this bridge.",
      "type" : "array",
      "minItems" : 0,
      "maxItems" : 2,
      "items" : {
        "$ref" : "#/definitions/BridgeSource"
      },
      "insertionOrder" : True
    },
    "IngressGatewayBridge" : {
      "type" : "object",
      "$ref" : "#/definitions/IngressGatewayBridge"
    },
    "EgressGatewayBridge" : {
      "type" : "object",
      "$ref" : "#/definitions/EgressGatewayBridge"
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name", "PlacementArn", "Sources" ],
  "readOnlyProperties" : [ "/properties/BridgeArn", "/properties/BridgeState" ],
  "primaryIdentifier" : [ "/properties/BridgeArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "mediaconnect:CreateBridge", "mediaconnect:DescribeBridge", "mediaconnect:AddBridgeOutputs", "mediaconnect:AddBridgeSources" ]
    },
    "read" : {
      "permissions" : [ "mediaconnect:DescribeBridge" ]
    },
    "update" : {
      "permissions" : [ "mediaconnect:DescribeBridge", "mediaconnect:UpdateBridge" ]
    },
    "delete" : {
      "permissions" : [ "mediaconnect:DescribeBridge", "mediaconnect:DeleteBridge", "mediaconnect:RemoveBridgeOutput", "mediaconnect:RemoveBridgeSource" ]
    },
    "list" : {
      "permissions" : [ "mediaconnect:ListBridges" ]
    }
  },
  "tagging" : {
    "taggable" : False
  }
}