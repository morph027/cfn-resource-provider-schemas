SCHEMA = {
  "typeName" : "AWS::SES::MailManagerIngressPoint",
  "description" : "Definition of AWS::SES::MailManagerIngressPoint Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ses-mailmanager",
  "definitions" : {
    "IngressPointConfiguration" : {
      "oneOf" : [ {
        "type" : "object",
        "title" : "SmtpPassword",
        "properties" : {
          "SmtpPassword" : {
            "type" : "string",
            "maxLength" : 64,
            "minLength" : 8,
            "pattern" : "^[A-Za-z0-9!@#$%^&*()_+\\-=\\[\\]{}|.,?]+$"
          }
        },
        "required" : [ "SmtpPassword" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "SecretArn",
        "properties" : {
          "SecretArn" : {
            "type" : "string",
            "pattern" : "^arn:(aws|aws-cn|aws-us-gov):secretsmanager:[a-z0-9-]+:\\d{12}:secret:[a-zA-Z0-9/_+=,.@-]+$"
          }
        },
        "required" : [ "SecretArn" ],
        "additionalProperties" : False
      } ]
    },
    "IngressPointStatus" : {
      "type" : "string",
      "enum" : [ "PROVISIONING", "DEPROVISIONING", "UPDATING", "ACTIVE", "CLOSED", "FAILED" ]
    },
    "IngressPointStatusToUpdate" : {
      "type" : "string",
      "enum" : [ "ACTIVE", "CLOSED" ]
    },
    "IngressPointType" : {
      "type" : "string",
      "enum" : [ "OPEN", "AUTH" ]
    },
    "IpType" : {
      "type" : "string",
      "enum" : [ "IPV4", "DUAL_STACK" ]
    },
    "NetworkConfiguration" : {
      "oneOf" : [ {
        "type" : "object",
        "title" : "PublicNetworkConfiguration",
        "properties" : {
          "PublicNetworkConfiguration" : {
            "$ref" : "#/definitions/PublicNetworkConfiguration"
          }
        },
        "required" : [ "PublicNetworkConfiguration" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "PrivateNetworkConfiguration",
        "properties" : {
          "PrivateNetworkConfiguration" : {
            "$ref" : "#/definitions/PrivateNetworkConfiguration"
          }
        },
        "required" : [ "PrivateNetworkConfiguration" ],
        "additionalProperties" : False
      } ]
    },
    "PrivateNetworkConfiguration" : {
      "type" : "object",
      "properties" : {
        "VpcEndpointId" : {
          "type" : "string",
          "pattern" : "^vpce-[a-zA-Z0-9]{17}$"
        }
      },
      "required" : [ "VpcEndpointId" ],
      "additionalProperties" : False
    },
    "PublicNetworkConfiguration" : {
      "type" : "object",
      "properties" : {
        "IpType" : {
          "allOf" : [ {
            "$ref" : "#/definitions/IpType"
          }, {
            "default" : "IPV4"
          } ]
        }
      },
      "required" : [ "IpType" ],
      "additionalProperties" : False
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "pattern" : "^[a-zA-Z0-9/_\\+=\\.:@\\-]+$"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0,
          "pattern" : "^[a-zA-Z0-9/_\\+=\\.:@\\-]*$"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ARecord" : {
      "type" : "string"
    },
    "TrafficPolicyId" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1
    },
    "IngressPointConfiguration" : {
      "$ref" : "#/definitions/IngressPointConfiguration"
    },
    "IngressPointArn" : {
      "type" : "string"
    },
    "IngressPointId" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1
    },
    "IngressPointName" : {
      "type" : "string",
      "maxLength" : 63,
      "minLength" : 3,
      "pattern" : "^[A-Za-z0-9_\\-]+$"
    },
    "NetworkConfiguration" : {
      "$ref" : "#/definitions/NetworkConfiguration"
    },
    "RuleSetId" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1
    },
    "Status" : {
      "$ref" : "#/definitions/IngressPointStatus"
    },
    "StatusToUpdate" : {
      "$ref" : "#/definitions/IngressPointStatusToUpdate"
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 200,
      "minItems" : 0
    },
    "Type" : {
      "$ref" : "#/definitions/IngressPointType"
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ses:TagResource", "ses:UntagResource" ]
  },
  "required" : [ "Type", "TrafficPolicyId", "RuleSetId" ],
  "readOnlyProperties" : [ "/properties/IngressPointId", "/properties/IngressPointArn", "/properties/Status", "/properties/ARecord" ],
  "createOnlyProperties" : [ "/properties/NetworkConfiguration", "/properties/Type" ],
  "writeOnlyProperties" : [ "/properties/IngressPointConfiguration" ],
  "primaryIdentifier" : [ "/properties/IngressPointId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ses:TagResource", "ses:ListTagsForResource", "ses:GetIngressPoint", "ses:CreateIngressPoint", "iam:CreateServiceLinkedRole", "ec2:DescribeVpcEndpoints" ]
    },
    "read" : {
      "permissions" : [ "ses:ListTagsForResource", "ses:GetIngressPoint" ]
    },
    "update" : {
      "permissions" : [ "ses:TagResource", "ses:UntagResource", "ses:ListTagsForResource", "ses:GetIngressPoint", "ses:UpdateIngressPoint" ]
    },
    "delete" : {
      "permissions" : [ "ses:GetIngressPoint", "ses:DeleteIngressPoint" ]
    },
    "list" : {
      "permissions" : [ "ses:ListIngressPoints" ]
    }
  },
  "additionalProperties" : False
}