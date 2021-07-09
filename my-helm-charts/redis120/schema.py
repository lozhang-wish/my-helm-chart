{
    'templateVersion': {
        'required': True,
        'type': 'string'
    },

    'name': {
        'required': True,
        'type': 'string'
    },

    'replicaCount': {
        'required': True,
        'type': 'integer'
    },

    'description': {
        'required': True,
        'type': 'string'
    },

    'image': {
        'required': True,
        'type': 'dict',
        'schema': {
            'repository': {
                'required': True,
                'type': 'string',
            },
            'pullPolicy': {
                'required': True,
                'type': 'string',
            }
        }
    },

    'ingress': {
        'required': True,
        'type': 'dict',
        'schema': {
            'enabled': {
                'required': True,
                'type': 'boolean'
            },
            'annotations': {
                'type': 'dict',
                'valueschema': {'type': 'string'}
            },
            'hosts': {
                'required': True,
                'type': 'list',
                'schema': {
                    'type': 'dict',
                    'schema': {
                        'host': {
                            'required': True,
                            'type': 'string',
                        },
                        'paths': {
                            'type': ['string', 'list']
                        }

                    }
                }
            }
        }
    }
}




