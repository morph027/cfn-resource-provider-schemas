SCHEMA = {
  "typeName" : "AWS::EC2::LocalGatewayRouteTableVirtualInterfaceGroupAssociation",
  "description" : "Resource Type definition for Local Gateway Route Table Virtual Interface Group Association which describes a local gateway route table virtual interface group association for a local gateway.",
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
    "LocalGatewayRouteTableVirtualInterfaceGroupAssociationId" : {
      "description" : "The ID of the local gateway route table virtual interface group association.",
      "type" : "string"
    },
    "LocalGatewayId" : {
      "description" : "The ID of the local gateway.",
      "type" : "string"
    },
    "LocalGatewayRouteTableId" : {
      "description" : "The ID of the local gateway route table.",
      "type" : "string"
    },
    "LocalGatewayRouteTableArn" : {
      "description" : "The ARN of the local gateway route table.",
      "type" : "string"
    },
    "LocalGatewayVirtualInterfaceGroupId" : {
      "description" : "The ID of the local gateway route table virtual interface group.",
      "type" : "string"
    },
    "OwnerId" : {
      "description" : "The owner of the local gateway route table virtual interface group association.",
      "type" : "string"
    },
    "State" : {
      "description" : "The state of the local gateway route table virtual interface group association.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "The tags for the local gateway route table virtual interface group association.",
      "$ref" : "#/definitions/Tags"
    }
  },
  "required" : [ "LocalGatewayRouteTableId", "LocalGatewayVirtualInterfaceGroupId" ],
  "createOnlyProperties" : [ "/properties/LocalGatewayRouteTableId", "/properties/LocalGatewayVirtualInterfaceGroupId" ],
  "readOnlyProperties" : [ "/properties/LocalGatewayRouteTableVirtualInterfaceGroupAssociationId", "/properties/LocalGatewayId", "/properties/LocalGatewayRouteTableArn", "/properties/OwnerId", "/properties/State" ],
  "primaryIdentifier" : [ "/properties/LocalGatewayRouteTableVirtualInterfaceGroupAssociationId" ],
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
      "permissions" : [ "ec2:CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation", "ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations", "ec2:CreateTags" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations", "ec2:DescribeTags" ]
    },
    "update" : {
      "permissions" : [ "ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations", "ec2:CreateTags", "ec2:DeleteTags", "ec2:DescribeTags" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociation", "ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations", "ec2:DeleteTags" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations" ]
    }
  },
  "replacementStrategy" : "delete_then_create",
  "additionalProperties" : False
}