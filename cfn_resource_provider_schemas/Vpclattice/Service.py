SCHEMA = {
  "typeName" : "AWS::VpcLattice::Service",
  "description" : "A service is any software application that can run on instances containers, or serverless functions within an account or virtual private cloud (VPC).",
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
      "pattern" : "^arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:service/svc-[0-9a-z]{17}$"
    },
    "AuthType" : {
      "type" : "string",
      "default" : "NONE",
      "enum" : [ "NONE", "AWS_IAM" ]
    },
    "CreatedAt" : {
      "type" : "string"
    },
    "DnsEntry" : {
      "$ref" : "#/definitions/DnsEntry"
    },
    "Id" : {
      "type" : "string",
      "maxLength" : 21,
      "minLength" : 21,
      "pattern" : "^svc-[0-9a-z]{17}$"
    },
    "LastUpdatedAt" : {
      "type" : "string"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 40,
      "minLength" : 3,
      "pattern" : "^(?!svc-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+$"
    },
    "Status" : {
      "type" : "string",
      "enum" : [ "ACTIVE", "CREATE_IN_PROGRESS", "DELETE_IN_PROGRESS", "CREATE_FAILED", "DELETE_FAILED" ]
    },
    "CertificateArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "pattern" : "^(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:certificate/[0-9a-z-]+)?$"
    },
    "CustomDomainName" : {
      "type" : "string",
      "maxLength" : 255,
      "minLength" : 3
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
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreatedAt", "/properties/DnsEntry/DomainName", "/properties/DnsEntry/HostedZoneId", "/properties/Id", "/properties/LastUpdatedAt", "/properties/Status" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/CustomDomainName" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "additionalIdentifiers" : [ [ "/properties/Id" ], [ "/properties/Name" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "vpc-lattice:CreateService", "vpc-lattice:GetService", "vpc-lattice:ListTagsForResource", "vpc-lattice:TagResource", "acm:DescribeCertificate", "acm:ListCertificates", "iam:CreateServiceLinkedRole" ]
    },
    "read" : {
      "permissions" : [ "vpc-lattice:GetService", "vpc-lattice:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "vpc-lattice:UpdateService", "vpc-lattice:TagResource", "vpc-lattice:UntagResource", "vpc-lattice:GetService", "vpc-lattice:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "vpc-lattice:DeleteService", "vpc-lattice:GetService", "vpc-lattice:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "vpc-lattice:ListServices" ]
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