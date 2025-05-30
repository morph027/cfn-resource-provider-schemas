SCHEMA = {
  "typeName" : "AWS::ResilienceHub::ResiliencyPolicy",
  "description" : "Resource Type Definition for Resiliency Policy.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-resiliencehub",
  "definitions" : {
    "FailurePolicy" : {
      "description" : "Failure Policy.",
      "type" : "object",
      "properties" : {
        "RtoInSecs" : {
          "description" : "RTO in seconds.",
          "type" : "integer"
        },
        "RpoInSecs" : {
          "description" : "RPO in seconds.",
          "type" : "integer"
        }
      },
      "required" : [ "RtoInSecs", "RpoInSecs" ],
      "additionalProperties" : False
    },
    "PolicyMap" : {
      "type" : "object",
      "properties" : {
        "AZ" : {
          "$ref" : "#/definitions/FailurePolicy"
        },
        "Hardware" : {
          "$ref" : "#/definitions/FailurePolicy"
        },
        "Software" : {
          "$ref" : "#/definitions/FailurePolicy"
        },
        "Region" : {
          "$ref" : "#/definitions/FailurePolicy"
        }
      },
      "required" : [ "AZ", "Hardware", "Software" ],
      "additionalProperties" : False
    },
    "TagValue" : {
      "type" : "string",
      "maxLength" : 256
    },
    "TagMap" : {
      "type" : "object",
      "patternProperties" : {
        ".{1,128}" : {
          "$ref" : "#/definitions/TagValue"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "PolicyName" : {
      "description" : "Name of Resiliency Policy.",
      "type" : "string",
      "pattern" : "^[A-Za-z0-9][A-Za-z0-9_\\-]{1,59}$"
    },
    "PolicyDescription" : {
      "description" : "Description of Resiliency Policy.",
      "type" : "string",
      "maxLength" : 500
    },
    "DataLocationConstraint" : {
      "type" : "string",
      "description" : "Data Location Constraint of the Policy.",
      "enum" : [ "AnyLocation", "SameContinent", "SameCountry" ]
    },
    "Tier" : {
      "type" : "string",
      "description" : "Resiliency Policy Tier.",
      "enum" : [ "MissionCritical", "Critical", "Important", "CoreServices", "NonCritical" ]
    },
    "Policy" : {
      "$ref" : "#/definitions/PolicyMap"
    },
    "PolicyArn" : {
      "type" : "string",
      "description" : "Amazon Resource Name (ARN) of the Resiliency Policy.",
      "pattern" : "^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$"
    },
    "Tags" : {
      "$ref" : "#/definitions/TagMap"
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "resiliencehub:TagResource", "resiliencehub:ListTagsForResource", "resiliencehub:UntagResource" ]
  },
  "additionalProperties" : False,
  "required" : [ "PolicyName", "Tier", "Policy" ],
  "readOnlyProperties" : [ "/properties/PolicyArn" ],
  "primaryIdentifier" : [ "/properties/PolicyArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "resiliencehub:CreateResiliencyPolicy", "resiliencehub:DescribeResiliencyPolicy", "resiliencehub:TagResource" ]
    },
    "update" : {
      "permissions" : [ "resiliencehub:DescribeResiliencyPolicy", "resiliencehub:UpdateResiliencyPolicy", "resiliencehub:TagResource", "resiliencehub:UntagResource", "resiliencehub:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "resiliencehub:DescribeResiliencyPolicy", "resiliencehub:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "resiliencehub:DeleteResiliencyPolicy", "resiliencehub:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "resiliencehub:ListResiliencyPolicies" ]
    }
  }
}