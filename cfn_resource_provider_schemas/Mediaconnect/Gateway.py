SCHEMA = {
  "typeName" : "AWS::MediaConnect::Gateway",
  "description" : "Resource schema for AWS::MediaConnect::Gateway",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-mediaconnect.git",
  "definitions" : {
    "GatewayNetwork" : {
      "description" : "The network settings for a gateway.",
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string",
          "description" : "The name of the network. This name is used to reference the network and must be unique among networks in this gateway."
        },
        "CidrBlock" : {
          "type" : "string",
          "description" : "A unique IP address range to use for this network. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16."
        }
      },
      "additionalProperties" : False,
      "required" : [ "Name", "CidrBlock" ]
    }
  },
  "properties" : {
    "Name" : {
      "description" : "The name of the gateway. This name can not be modified after the gateway is created.",
      "type" : "string"
    },
    "GatewayArn" : {
      "description" : "The Amazon Resource Name (ARN) of the gateway.",
      "type" : "string"
    },
    "GatewayState" : {
      "description" : "The current status of the gateway.",
      "type" : "string",
      "enum" : [ "CREATING", "ACTIVE", "UPDATING", "ERROR", "DELETING", "DELETED" ]
    },
    "EgressCidrBlocks" : {
      "description" : "The range of IP addresses that contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.",
      "type" : "array",
      "items" : {
        "type" : "string"
      },
      "insertionOrder" : True
    },
    "Networks" : {
      "type" : "array",
      "description" : "The list of networks in the gateway.",
      "minItems" : 1,
      "maxItems" : 4,
      "items" : {
        "$ref" : "#/definitions/GatewayNetwork"
      },
      "insertionOrder" : True
    }
  },
  "required" : [ "Name", "EgressCidrBlocks", "Networks" ],
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/GatewayArn", "/properties/GatewayState" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/EgressCidrBlocks", "/properties/Networks" ],
  "primaryIdentifier" : [ "/properties/GatewayArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:CreateServiceLinkedRole", "mediaconnect:CreateGateway", "mediaconnect:DescribeGateway" ]
    },
    "read" : {
      "permissions" : [ "mediaconnect:DescribeGateway" ]
    },
    "delete" : {
      "permissions" : [ "iam:CreateServiceLinkedRole", "mediaconnect:DescribeGateway", "mediaconnect:DeleteGateway" ]
    },
    "list" : {
      "permissions" : [ "mediaconnect:ListGateways" ]
    }
  },
  "tagging" : {
    "taggable" : False
  }
}