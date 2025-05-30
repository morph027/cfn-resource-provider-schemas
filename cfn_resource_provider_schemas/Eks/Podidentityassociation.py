SCHEMA = {
  "tagging" : {
    "permissions" : [ "eks:TagResource", "eks:UntagResource" ],
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "tagProperty" : "/properties/Tags",
    "cloudFormationSystemTags" : True
  },
  "typeName" : "AWS::EKS::PodIdentityAssociation",
  "readOnlyProperties" : [ "/properties/AssociationArn", "/properties/AssociationId" ],
  "description" : "An object representing an Amazon EKS PodIdentityAssociation.",
  "createOnlyProperties" : [ "/properties/ClusterName", "/properties/Namespace", "/properties/ServiceAccount" ],
  "primaryIdentifier" : [ "/properties/AssociationArn" ],
  "required" : [ "ClusterName", "RoleArn", "Namespace", "ServiceAccount" ],
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-eks.git",
  "handlers" : {
    "read" : {
      "permissions" : [ "eks:DescribePodIdentityAssociation" ]
    },
    "create" : {
      "permissions" : [ "eks:CreatePodIdentityAssociation", "eks:DescribePodIdentityAssociation", "eks:TagResource", "iam:PassRole", "iam:GetRole" ]
    },
    "update" : {
      "permissions" : [ "eks:DescribePodIdentityAssociation", "eks:UpdatePodIdentityAssociation", "eks:TagResource", "eks:UntagResource", "iam:PassRole", "iam:GetRole" ]
    },
    "list" : {
      "permissions" : [ "eks:ListPodIdentityAssociations" ],
      "handlerSchema" : {
        "properties" : {
          "ClusterName" : {
            "$ref" : "resource-schema.json#/properties/ClusterName"
          }
        },
        "required" : [ "ClusterName" ]
      }
    },
    "delete" : {
      "permissions" : [ "eks:DeletePodIdentityAssociation", "eks:DescribePodIdentityAssociation" ]
    }
  },
  "additionalProperties" : False,
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Value" : {
          "minLength" : 0,
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string",
          "maxLength" : 256
        },
        "Key" : {
          "minLength" : 1,
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string",
          "maxLength" : 128
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "AssociationArn" : {
      "description" : "The ARN of the pod identity association.",
      "type" : "string"
    },
    "ServiceAccount" : {
      "description" : "The Kubernetes service account that the pod identity association is created for.",
      "type" : "string"
    },
    "ClusterName" : {
      "minLength" : 1,
      "description" : "The cluster that the pod identity association is created for.",
      "type" : "string"
    },
    "RoleArn" : {
      "description" : "The IAM role ARN that the pod identity association is created for.",
      "type" : "string"
    },
    "Namespace" : {
      "description" : "The Kubernetes namespace that the pod identity association is created for.",
      "type" : "string"
    },
    "AssociationId" : {
      "minLength" : 1,
      "description" : "The ID of the pod identity association.",
      "type" : "string"
    },
    "Tags" : {
      "uniqueItems" : True,
      "description" : "An array of key-value pairs to apply to this resource.",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "replacementStrategy" : "create_then_delete"
}