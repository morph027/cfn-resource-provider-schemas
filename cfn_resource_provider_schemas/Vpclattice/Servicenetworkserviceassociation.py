SCHEMA = {
  "typeName" : "AWS::VpcLattice::ServiceNetworkServiceAssociation",
  "description" : "Associates a service with a service network.",
  "additionalProperties" : False,
  "definitions" : {
    "DnsEntry" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DomainName" : {
          "type" : "string"
        },
        "HostedZoneId" : {
          "type" : "string"
        }
      }
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
      "pattern" : "^arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:servicenetworkserviceassociation/snsa-[0-9a-z]{17}$"
    },
    "CreatedAt" : {
      "type" : "string"
    },
    "DnsEntry" : {
      "$ref" : "#/definitions/DnsEntry"
    },
    "Id" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 17,
      "pattern" : "^snsa-[0-9a-z]{17}$"
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
    "ServiceArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:service/svc-[0-9a-z]{17}$"
    },
    "ServiceId" : {
      "type" : "string",
      "maxLength" : 21,
      "minLength" : 21,
      "pattern" : "^svc-[0-9a-z]{17}$"
    },
    "ServiceIdentifier" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^((svc-[0-9a-z]{17})|(arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:service/svc-[0-9a-z]{17}))$"
    },
    "ServiceName" : {
      "type" : "string",
      "maxLength" : 40,
      "minLength" : 3,
      "pattern" : "^(?!svc-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+$"
    },
    "Status" : {
      "type" : "string",
      "enum" : [ "CREATE_IN_PROGRESS", "ACTIVE", "DELETE_IN_PROGRESS", "CREATE_FAILED", "DELETE_FAILED" ]
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
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreatedAt", "/properties/DnsEntry/DomainName", "/properties/DnsEntry/HostedZoneId", "/properties/Id", "/properties/ServiceNetworkArn", "/properties/ServiceNetworkId", "/properties/ServiceNetworkName", "/properties/ServiceArn", "/properties/ServiceId", "/properties/ServiceName", "/properties/Status" ],
  "writeOnlyProperties" : [ "/properties/ServiceNetworkIdentifier", "/properties/ServiceIdentifier" ],
  "createOnlyProperties" : [ "/properties/ServiceNetworkIdentifier", "/properties/ServiceIdentifier" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "additionalIdentifiers" : [ [ "/properties/Id" ], [ "/properties/ServiceNetworkIdentifier", "/properties/ServiceIdentifier" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "vpc-lattice:CreateServiceNetworkServiceAssociation", "vpc-lattice:GetServiceNetworkServiceAssociation", "vpc-lattice:TagResource", "vpc-lattice:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "vpc-lattice:GetServiceNetworkServiceAssociation", "vpc-lattice:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "vpc-lattice:TagResource", "vpc-lattice:UntagResource", "vpc-lattice:GetServiceNetworkServiceAssociation", "vpc-lattice:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "vpc-lattice:DeleteServiceNetworkServiceAssociation", "vpc-lattice:GetServiceNetworkServiceAssociation", "vpc-lattice:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "vpc-lattice:ListServiceNetworkServiceAssociations" ],
      "handlerSchema" : {
        "properties" : {
          "ServiceNetworkIdentifier" : {
            "type" : "string",
            "maxLength" : 2048,
            "minLength" : 20,
            "pattern" : "^((sn-[0-9a-z]{17})|(arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:servicenetwork/sn-[0-9a-z]{17}))$"
          },
          "ServiceIdentifier" : {
            "type" : "string",
            "maxLength" : 2048,
            "minLength" : 20,
            "pattern" : "^((svc-[0-9a-z]{17})|(arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:service/svc-[0-9a-z]{17}))$"
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