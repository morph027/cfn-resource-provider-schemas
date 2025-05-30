SCHEMA = {
  "typeName" : "AWS::EC2::LocalGatewayRouteTable",
  "description" : "Resource Type definition for Local Gateway Route Table which describes a route table for a local gateway.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2-lgw.git",
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
    "LocalGatewayRouteTableId" : {
      "description" : "The ID of the local gateway route table.",
      "type" : "string"
    },
    "LocalGatewayRouteTableArn" : {
      "description" : "The ARN of the local gateway route table.",
      "type" : "string"
    },
    "LocalGatewayId" : {
      "description" : "The ID of the local gateway.",
      "type" : "string"
    },
    "OutpostArn" : {
      "description" : "The ARN of the outpost.",
      "type" : "string"
    },
    "OwnerId" : {
      "description" : "The owner of the local gateway route table.",
      "type" : "string"
    },
    "State" : {
      "description" : "The state of the local gateway route table.",
      "type" : "string"
    },
    "Mode" : {
      "description" : "The mode of the local gateway route table.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "The tags for the local gateway route table.",
      "$ref" : "#/definitions/Tags"
    }
  },
  "required" : [ "LocalGatewayId" ],
  "createOnlyProperties" : [ "/properties/LocalGatewayId", "/properties/Mode" ],
  "readOnlyProperties" : [ "/properties/LocalGatewayRouteTableId", "/properties/LocalGatewayRouteTableArn", "/properties/OutpostArn", "/properties/OwnerId", "/properties/State" ],
  "primaryIdentifier" : [ "/properties/LocalGatewayRouteTableId" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ec2:DeleteTags", "ec2:CreateTags", "ec2:DescribeTags" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateLocalGatewayRouteTable", "ec2:DescribeLocalGatewayRouteTables", "ec2:CreateTags" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeLocalGatewayRouteTables", "ec2:DescribeTags" ]
    },
    "update" : {
      "permissions" : [ "ec2:DescribeLocalGatewayRouteTables", "ec2:CreateTags", "ec2:DeleteTags", "ec2:DescribeTags" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteLocalGatewayRouteTable", "ec2:DescribeLocalGatewayRouteTables", "ec2:DeleteTags" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeLocalGatewayRouteTables" ]
    }
  },
  "replacementStrategy" : "delete_then_create",
  "additionalProperties" : False
}