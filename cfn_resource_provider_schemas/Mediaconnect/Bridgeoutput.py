SCHEMA = {
  "typeName" : "AWS::MediaConnect::BridgeOutput",
  "description" : "Resource schema for AWS::MediaConnect::BridgeOutput",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-mediaconnect.git",
  "definitions" : {
    "BridgeNetworkOutput" : {
      "type" : "object",
      "description" : "The output of the bridge. A network output is delivered to your premises.",
      "properties" : {
        "Protocol" : {
          "type" : "string",
          "enum" : [ "rtp-fec", "rtp", "udp" ],
          "description" : "The network output protocol."
        },
        "IpAddress" : {
          "type" : "string",
          "description" : "The network output IP Address."
        },
        "Port" : {
          "type" : "integer",
          "description" : "The network output port."
        },
        "NetworkName" : {
          "type" : "string",
          "description" : "The network output's gateway network name."
        },
        "Ttl" : {
          "type" : "integer",
          "description" : "The network output TTL."
        }
      },
      "required" : [ "Protocol", "IpAddress", "Port", "NetworkName", "Ttl" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "BridgeArn" : {
      "description" : "The Amazon Resource Number (ARN) of the bridge.",
      "type" : "string"
    },
    "NetworkOutput" : {
      "description" : "The output of the bridge.",
      "$ref" : "#/definitions/BridgeNetworkOutput"
    },
    "Name" : {
      "type" : "string",
      "description" : "The network output name."
    }
  },
  "additionalProperties" : False,
  "required" : [ "BridgeArn", "Name", "NetworkOutput" ],
  "createOnlyProperties" : [ "/properties/BridgeArn", "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/BridgeArn", "/properties/Name" ],
  "propertyTransform" : {
    "/properties/Name" : "$join([\"Output:\",Name])"
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "mediaconnect:AddBridgeOutputs", "mediaconnect:DescribeBridge" ]
    },
    "read" : {
      "permissions" : [ "mediaconnect:DescribeBridge" ]
    },
    "update" : {
      "permissions" : [ "mediaconnect:DescribeBridge", "mediaconnect:UpdateBridgeOutput" ]
    },
    "delete" : {
      "permissions" : [ "mediaconnect:RemoveBridgeOutput" ]
    }
  },
  "tagging" : {
    "taggable" : False
  }
}