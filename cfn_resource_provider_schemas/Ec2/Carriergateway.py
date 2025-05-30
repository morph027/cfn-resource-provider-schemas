SCHEMA = {
  "typeName" : "AWS::EC2::CarrierGateway",
  "description" : "Resource Type definition for Carrier Gateway which describes the Carrier Gateway resource",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 127,
          "pattern" : "^(?!aws:.*)"
        },
        "Value" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255,
          "pattern" : "^(?!aws:.*)"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "CarrierGatewayId" : {
      "description" : "The ID of the carrier gateway.",
      "type" : "string"
    },
    "State" : {
      "description" : "The state of the carrier gateway.",
      "type" : "string"
    },
    "VpcId" : {
      "description" : "The ID of the VPC.",
      "type" : "string"
    },
    "OwnerId" : {
      "description" : "The ID of the owner.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "The tags for the carrier gateway.",
      "$ref" : "#/definitions/Tags"
    }
  },
  "required" : [ "VpcId" ],
  "createOnlyProperties" : [ "/properties/VpcId" ],
  "readOnlyProperties" : [ "/properties/CarrierGatewayId", "/properties/OwnerId", "/properties/State" ],
  "primaryIdentifier" : [ "/properties/CarrierGatewayId" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ec2:CreateTags", "ec2:DeleteTags", "ec2:DescribeTags" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateCarrierGateway", "ec2:DescribeCarrierGateways", "ec2:CreateTags" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeCarrierGateways", "ec2:DescribeTags" ]
    },
    "update" : {
      "permissions" : [ "ec2:DescribeCarrierGateways", "ec2:CreateTags", "ec2:DeleteTags", "ec2:DescribeTags" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteCarrierGateway", "ec2:DescribeCarrierGateways", "ec2:DeleteTags" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeCarrierGateways" ]
    }
  },
  "additionalProperties" : False
}