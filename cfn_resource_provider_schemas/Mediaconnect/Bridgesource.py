SCHEMA = {
  "typeName" : "AWS::MediaConnect::BridgeSource",
  "description" : "Resource schema for AWS::MediaConnect::BridgeSource",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-mediaconnect.git",
  "definitions" : {
    "BridgeFlowSource" : {
      "type" : "object",
      "description" : "The source of the bridge. A flow source originates in MediaConnect as an existing cloud flow.",
      "properties" : {
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
      "required" : [ "FlowArn" ]
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
      "required" : [ "Protocol", "MulticastIp", "Port", "NetworkName" ],
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
    }
  },
  "properties" : {
    "Name" : {
      "type" : "string",
      "description" : "The name of the source."
    },
    "BridgeArn" : {
      "description" : "The Amazon Resource Number (ARN) of the bridge.",
      "type" : "string"
    },
    "FlowSource" : {
      "$ref" : "#/definitions/BridgeFlowSource"
    },
    "NetworkSource" : {
      "$ref" : "#/definitions/BridgeNetworkSource"
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name", "BridgeArn" ],
  "createOnlyProperties" : [ "/properties/BridgeArn", "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/BridgeArn", "/properties/Name" ],
  "propertyTransform" : {
    "/properties/Name" : "$join([\"Source:\",Name])"
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "mediaconnect:AddBridgeSources", "mediaconnect:DescribeBridge" ]
    },
    "read" : {
      "permissions" : [ "mediaconnect:DescribeBridge" ]
    },
    "update" : {
      "permissions" : [ "mediaconnect:DescribeBridge", "mediaconnect:UpdateBridgeSource" ]
    },
    "delete" : {
      "permissions" : [ "mediaconnect:RemoveBridgeSource" ]
    }
  },
  "tagging" : {
    "taggable" : False
  }
}