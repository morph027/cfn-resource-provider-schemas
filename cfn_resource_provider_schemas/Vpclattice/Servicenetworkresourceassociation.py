SCHEMA = {
  "typeName" : "AWS::VpcLattice::ServiceNetworkResourceAssociation",
  "description" : "VpcLattice ServiceNetworkResourceAssociation CFN resource",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
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
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Id" : {
      "type" : "string",
      "minLength" : 22,
      "maxLength" : 22,
      "pattern" : "^snra-[0-9a-f]{17}$"
    },
    "Arn" : {
      "type" : "string",
      "minLength" : 22,
      "maxLength" : 2048,
      "pattern" : "^arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:servicenetworkresourceassociation/snra-[0-9a-f]{17}$"
    },
    "ResourceConfigurationId" : {
      "type" : "string",
      "minLength" : 17,
      "maxLength" : 2048,
      "pattern" : "^rcfg-[0-9a-z]{17}$"
    },
    "ServiceNetworkId" : {
      "type" : "string",
      "minLength" : 3,
      "maxLength" : 2048,
      "pattern" : "^((sn-[0-9a-z]{17})|(arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:servicenetwork/sn-[0-9a-z]{17}))$"
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
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/ResourceConfigurationId", "/properties/ServiceNetworkId" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "additionalIdentifiers" : [ [ "/properties/Id" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "vpc-lattice:CreateServiceNetworkResourceAssociation", "vpc-lattice:GetServiceNetworkResourceAssociation", "vpc-lattice:TagResource", "vpc-lattice:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "vpc-lattice:GetServiceNetworkResourceAssociation", "vpc-lattice:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "vpc-lattice:TagResource", "vpc-lattice:UntagResource", "vpc-lattice:GetServiceNetworkResourceAssociation", "vpc-lattice:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "vpc-lattice:DeleteServiceNetworkResourceAssociation", "vpc-lattice:GetServiceNetworkResourceAssociation", "vpc-lattice:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "vpc-lattice:ListServiceNetworkResourceAssociations" ]
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