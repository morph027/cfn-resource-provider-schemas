SCHEMA = {
  "typeName" : "AWS::VpcLattice::ServiceNetwork",
  "description" : "A service network is a logical boundary for a collection of services. You can associate services and VPCs with a service network.",
  "additionalProperties" : False,
  "definitions" : {
    "SharingConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "enabled" : {
          "type" : "boolean"
        }
      },
      "required" : [ "enabled" ]
    },
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
      "pattern" : "^arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:servicenetwork/sn-[0-9a-z]{17}$"
    },
    "CreatedAt" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string",
      "maxLength" : 20,
      "minLength" : 20,
      "pattern" : "^sn-[0-9a-z]{17}$"
    },
    "LastUpdatedAt" : {
      "type" : "string"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 63,
      "minLength" : 3,
      "pattern" : "^(?!servicenetwork-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+$"
    },
    "AuthType" : {
      "type" : "string",
      "default" : "NONE",
      "enum" : [ "NONE", "AWS_IAM" ]
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
    },
    "SharingConfig" : {
      "$ref" : "#/definitions/SharingConfig"
    }
  },
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreatedAt", "/properties/Id", "/properties/LastUpdatedAt" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "additionalIdentifiers" : [ [ "/properties/Id" ], [ "/properties/Name" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "vpc-lattice:GetServiceNetwork", "vpc-lattice:ListTagsForResource", "vpc-lattice:CreateServiceNetwork", "vpc-lattice:TagResource", "iam:CreateServiceLinkedRole" ]
    },
    "read" : {
      "permissions" : [ "vpc-lattice:GetServiceNetwork", "vpc-lattice:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "vpc-lattice:GetServiceNetwork", "vpc-lattice:UpdateServiceNetwork", "vpc-lattice:TagResource", "vpc-lattice:UntagResource", "vpc-lattice:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "vpc-lattice:DeleteServiceNetwork", "vpc-lattice:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "vpc-lattice:ListServiceNetworks" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "vpc-lattice:UntagResource", "vpc-lattice:TagResource", "vpc-lattice:ListTagsForResource" ]
  }
}