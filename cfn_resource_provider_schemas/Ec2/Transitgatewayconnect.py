SCHEMA = {
  "typeName" : "AWS::EC2::TransitGatewayConnect",
  "description" : "The AWS::EC2::TransitGatewayConnect type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-myservice",
  "properties" : {
    "TransitGatewayAttachmentId" : {
      "description" : "The ID of the Connect attachment.",
      "type" : "string"
    },
    "TransportTransitGatewayAttachmentId" : {
      "description" : "The ID of the attachment from which the Connect attachment was created.",
      "type" : "string"
    },
    "TransitGatewayId" : {
      "description" : "The ID of the transit gateway.",
      "type" : "string"
    },
    "State" : {
      "description" : "The state of the attachment.",
      "type" : "string"
    },
    "CreationTime" : {
      "description" : "The creation time.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "The tags for the attachment.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Options" : {
      "$ref" : "#/definitions/TransitGatewayConnectOptions",
      "description" : "The Connect attachment options."
    }
  },
  "required" : [ "TransportTransitGatewayAttachmentId", "Options" ],
  "definitions" : {
    "TransitGatewayConnectOptions" : {
      "type" : "object",
      "properties" : {
        "Protocol" : {
          "description" : "The tunnel protocol.",
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "description" : "The key of the tag. Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws:.",
          "type" : "string"
        },
        "Value" : {
          "description" : "The value of the tag. Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.",
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ec2:CreateTags", "ec2:DeleteTags" ]
  },
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/TransitGatewayAttachmentId", "/properties/State", "/properties/CreationTime", "/properties/TransitGatewayId" ],
  "createOnlyProperties" : [ "/properties/TransportTransitGatewayAttachmentId", "/properties/Options" ],
  "primaryIdentifier" : [ "/properties/TransitGatewayAttachmentId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateTransitGatewayConnect", "ec2:DescribeTransitGatewayConnects", "ec2:CreateTags", "ec2:DescribeTags" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeTransitGatewayConnects", "ec2:DescribeTags" ]
    },
    "update" : {
      "permissions" : [ "ec2:DescribeTransitGatewayConnects", "ec2:DeleteTags", "ec2:CreateTags", "ec2:DescribeTags" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteTransitGatewayConnect", "ec2:DescribeTransitGatewayConnects", "ec2:DeleteTags", "ec2:DescribeTags" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeTransitGatewayConnects", "ec2:DescribeTags" ]
    }
  }
}