SCHEMA = {
  "typeName" : "AWS::VpcLattice::ServiceNetworkVpcAssociation",
  "description" : "Associates a VPC with a service network.",
  "additionalProperties" : False,
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:servicenetworkvpcassociation/snva-[0-9a-z]{17}$"
    },
    "CreatedAt" : {
      "type" : "string"
    },
    "SecurityGroupIds" : {
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "type" : "string",
        "maxLength" : 200,
        "minLength" : 0,
        "pattern" : "^sg-(([0-9a-z]{8})|([0-9a-z]{17}))$"
      }
    },
    "Id" : {
      "type" : "string",
      "maxLength" : 22,
      "minLength" : 22,
      "pattern" : "^snva-[0-9a-z]{17}$"
    },
    "ServiceNetworkArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:servicenetwork/sn-[0-9a-z]{17}$"
    },
    "ServiceNetworkId" : {
      "type" : "string",
      "maxLength" : 20,
      "minLength" : 20,
      "pattern" : "^sn-[0-9a-z]{17}$"
    },
    "ServiceNetworkIdentifier" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^((sn-[0-9a-z]{17})|(arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:servicenetwork/sn-[0-9a-z]{17}))$"
    },
    "ServiceNetworkName" : {
      "type" : "string",
      "maxLength" : 63,
      "minLength" : 3,
      "pattern" : "^(?!servicenetwork-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+$"
    },
    "Status" : {
      "type" : "string",
      "enum" : [ "CREATE_IN_PROGRESS", "ACTIVE", "UPDATE_IN_PROGRESS", "DELETE_IN_PROGRESS", "CREATE_FAILED", "DELETE_FAILED" ]
    },
    "VpcId" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 5,
      "pattern" : "^vpc-(([0-9a-z]{8})|([0-9a-z]{17}))$"
    },
    "VpcIdentifier" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 5,
      "pattern" : "^vpc-(([0-9a-z]{8})|([0-9a-z]{17}))$"
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "minItems" : 0,
      "maxItems" : 50,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreatedAt", "/properties/Id", "/properties/ServiceNetworkArn", "/properties/ServiceNetworkId", "/properties/ServiceNetworkName", "/properties/Status", "/properties/VpcId" ],
  "writeOnlyProperties" : [ "/properties/ServiceNetworkIdentifier", "/properties/VpcIdentifier" ],
  "createOnlyProperties" : [ "/properties/ServiceNetworkIdentifier", "/properties/VpcIdentifier" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "additionalIdentifiers" : [ [ "/properties/Id" ], [ "/properties/ServiceNetworkIdentifier", "/properties/VpcIdentifier" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "vpc-lattice:CreateServiceNetworkVpcAssociation", "vpc-lattice:GetServiceNetworkVpcAssociation", "vpc-lattice:ListServiceNetworkVpcAssociations", "vpc-lattice:ListTagsForResource", "ec2:DescribeSecurityGroups", "ec2:DescribeVpcs", "vpc-lattice:TagResource" ]
    },
    "read" : {
      "permissions" : [ "vpc-lattice:GetServiceNetworkVpcAssociation", "vpc-lattice:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "vpc-lattice:TagResource", "vpc-lattice:UntagResource", "vpc-lattice:GetServiceNetworkVpcAssociation", "vpc-lattice:UpdateServiceNetworkVpcAssociation", "ec2:DescribeSecurityGroups", "vpc-lattice:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "vpc-lattice:DeleteServiceNetworkVpcAssociation", "vpc-lattice:GetServiceNetworkVpcAssociation", "vpc-lattice:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "vpc-lattice:ListServiceNetworkVpcAssociations" ],
      "handlerSchema" : {
        "properties" : {
          "ServiceNetworkIdentifier" : {
            "type" : "string",
            "maxLength" : 2048,
            "minLength" : 20,
            "pattern" : "^((sn-[0-9a-z]{17})|(arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:servicenetwork/sn-[0-9a-z]{17}))$"
          },
          "VpcIdentifier" : {
            "type" : "string",
            "maxLength" : 2048,
            "minLength" : 5,
            "pattern" : "^vpc-(([0-9a-z]{8})|([0-9a-z]{17}))$"
          }
        },
        "required" : [ ]
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "vpc-lattice:UntagResource", "vpc-lattice:TagResource", "vpc-lattice:ListTagsForResource" ]
  }
}