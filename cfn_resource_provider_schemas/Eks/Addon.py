SCHEMA = {
  "typeName" : "AWS::EKS::Addon",
  "description" : "Resource Schema for AWS::EKS::Addon",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-eks.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 127
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 255
        }
      },
      "required" : [ "Key", "Value" ]
    },
    "PodIdentityAssociation" : {
      "description" : "A pod identity to associate with an add-on.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ServiceAccount" : {
          "type" : "string",
          "description" : "The Kubernetes service account that the pod identity association is created for."
        },
        "RoleArn" : {
          "type" : "string",
          "pattern" : "^arn:aws(-cn|-us-gov|-iso(-[a-z])?)?:iam::\\d{12}:(role)\\/*",
          "description" : "The IAM role ARN that the pod identity association is created for."
        }
      },
      "required" : [ "ServiceAccount", "RoleArn" ]
    }
  },
  "properties" : {
    "ClusterName" : {
      "description" : "Name of Cluster",
      "type" : "string",
      "minLength" : 1
    },
    "AddonName" : {
      "description" : "Name of Addon",
      "type" : "string",
      "minLength" : 1
    },
    "AddonVersion" : {
      "description" : "Version of Addon",
      "type" : "string",
      "minLength" : 1
    },
    "PreserveOnDelete" : {
      "description" : "PreserveOnDelete parameter value",
      "type" : "boolean"
    },
    "ResolveConflicts" : {
      "description" : "Resolve parameter value conflicts",
      "type" : "string",
      "minLength" : 1,
      "enum" : [ "NONE", "OVERWRITE", "PRESERVE" ]
    },
    "ServiceAccountRoleArn" : {
      "description" : "IAM role to bind to the add-on's service account",
      "type" : "string",
      "minLength" : 1
    },
    "PodIdentityAssociations" : {
      "description" : "An array of pod identities to apply to this add-on.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/PodIdentityAssociation"
      }
    },
    "ConfigurationValues" : {
      "description" : "The configuration values to use with the add-on",
      "type" : "string",
      "minLength" : 1
    },
    "Arn" : {
      "description" : "Amazon Resource Name (ARN) of the add-on",
      "type" : "string"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "eks:TagResource", "eks:UntagResource" ]
  },
  "additionalProperties" : False,
  "required" : [ "ClusterName", "AddonName" ],
  "primaryIdentifier" : [ "/properties/ClusterName", "/properties/AddonName" ],
  "createOnlyProperties" : [ "/properties/ClusterName", "/properties/AddonName" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "writeOnlyProperties" : [ "/properties/ResolveConflicts", "/properties/PreserveOnDelete", "/properties/PodIdentityAssociations" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "eks:CreateAddon", "eks:DescribeAddon", "eks:TagResource", "iam:PassRole", "iam:GetRole", "eks:CreatePodIdentityAssociation" ]
    },
    "read" : {
      "permissions" : [ "eks:DescribeAddon" ]
    },
    "delete" : {
      "permissions" : [ "eks:DeleteAddon", "eks:DescribeAddon", "eks:DeletePodIdentityAssociation" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "ClusterName" : {
            "$ref" : "resource-schema.json#/properties/ClusterName"
          }
        },
        "required" : [ "ClusterName" ]
      },
      "permissions" : [ "eks:ListAddons" ]
    },
    "update" : {
      "permissions" : [ "iam:PassRole", "iam:GetRole", "eks:UpdateAddon", "eks:DescribeAddon", "eks:DescribeUpdate", "eks:TagResource", "eks:UntagResource", "eks:CreatePodIdentityAssociation", "eks:DeletePodIdentityAssociation", "eks:UpdatePodIdentityAssociation" ]
    }
  }
}